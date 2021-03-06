NAME = 'Extract USD'
ORDER = 2
VALID = True
TYPE = 'extractor'
OWNER = 'Subin Gopi'
COMMENTS = 'To create USD'
VERSION = '0.0.0'
LAST_MODIFIED = 'April 14, 2020'


def execute(**kwargs):   
    values = []
    message = ''
    
    return True, values, message


def trail():    
    return True, [], 'trail run'

    
import os
import copy
import json
import time
import shutil
import getpass
import tempfile

from studio_usd_pipe import resource
from studio_usd_pipe.core.tmp import mayapack
from studio_usd_pipe.core import database
from studio_usd_pipe.core import preferences

reload(mayapack)
reload(database)


class Asset(object):
    
    def __init__(self, subfield=None):      
        self.standalone = False
        self.data = {}        
        self.subfield = subfield        
        self.width, self.height = 640, 400
        self.entity = 'assets'         
        self.temp_entity = 'studio_asset'      
        self.asset_ids = [
            'sentity',
            'scaption',
            'stype',
            'stag',
            'sversion',
            'smodified',
            'slocation',
            'sdescription'
            ]

        self.mpack = mayapack.Pack()
        self.set_inputs()
        self.dbs = database.DataBase(self.entity)
        
    def get(self):
        data = self.dbs.get()        
        db_data = {}
        for table, contents in data.items():    
            keys = {
                'tag': contents['tag'],
                'caption': contents['caption'],
                'user': contents['user'],
                'date': contents['date'],
                'location': contents['location'],
                'type': contents['type']        
                }
            if contents['caption'] not in db_data:
                db_data.setdefault(contents['caption'], {})
            if contents['subfield'] not in db_data[contents['caption']]:
                db_data[contents['caption']].setdefault(contents['subfield'], {}) 
            db_data[contents['caption']][contents['subfield']].setdefault(
                contents['version'], keys)
        return db_data
    
    def get_subfields(self, caption, db_data=None):
        if not db_data:
            db_data = self.get()
        subfield_data = {}
        if caption in db_data:
            subfield_data = db_data[caption]
        return subfield_data
    
    def get_version_data(self, caption, subfield, db_data=None):
        subfield_data = self.get_subfields(caption, db_data=db_data)
        version_data = {}
        for k, v in subfield_data.items():    
            if k != subfield:
                continue        
            version_data.update(v)        
        return version_data

    def get_asset_data(self, caption, subfield, version, db_data=None):        
        data = self.get_subfields(caption, db_data=db_data)
        if subfield not in data:
            raise ValueError(
                'Not found <{}> in the database'.format(subfield))
        if version not in data[subfield]:
            raise ValueError(
                'Not found <{} {}> in the database'.format(subfield, version))
        return data[subfield][version]
    
    def get_asset_more_data(self, caption, subfield, version):
        manifest_path = os.path.join(
            self.show_path,
            self.entity,
            caption,
            subfield,
            version,
            '{}.manifest'.format(caption)
            )
        data = resource.get_input_data(manifest_path)
        sorted_data = copy.deepcopy(data)
        extrude = ['caption', 'tag', 'user', 'date', 'location', 'type']
        for each in data:
            if each not in extrude:
                continue
            sorted_data.pop(each)
        return sorted_data
    
    def get_specific_key_captions(self, key, db_data=None):
        if not db_data:
            db_data = self.get()
        tag_data = {}
        for asset, subfields in db_data.items():
            for subfield in subfields:
                for version in subfields[subfield]:
                    specific_key = subfields[subfield][version][key]                    
                    if specific_key in tag_data:                    
                        if asset in tag_data[specific_key]:
                            continue                    
                    tag_data.setdefault(specific_key, []).append(asset)
        return tag_data    

    def set_inputs(self):
        pref = preferences.Preferences()
        self.input_data = pref.get()        
        self.db_directory = self.input_data['database_directory']   
        self.show_icon = self.input_data['show_icon']
        self.mayapy = self.input_data['mayapy_directory']
        self.show_path = self.input_data['show_directory']
    
    def pack(self, bundle, **kwargs):
        '''
            import time
            from studio_usd_pipe.core import asset
            reload(asset)        
            asset = asset.Asset(subfield='model')        
            bundle = {
                'source_file': '/venture/shows/my_hero/dumps/batman_finB.ma',
                'caption': 'batman',
                'version': '0.0.0',
                'thumbnail': '/local/references/images/btas_batmodel_03.jpg',
                'type': 'interactive',
                'tag': 'character',
                'description': 'test publish',
                'time_stamp': time.time()
                }        
            asset.pack(bundle)         
        '''
        print json.dumps(bundle, indent=4)
        self.data = {}
        self.source_maya = bundle['source_file']
        self.caption = bundle['caption']
        self.version = bundle['version'] 
        self.thumbnail = None
        if 'thumbnail' in bundle:
            self.thumbnail = bundle['thumbnail']
        self.type = bundle['type']
        self.tag = bundle['tag']
        self.description = bundle['description']   
        self.time_stamp = bundle['time_stamp'] 
        
        self.publish_path = os.path.join(
            self.show_path,
            self.entity,
            self.caption,
            self.subfield,
            self.version
            )
        
        self.temp_pack_path = self.make_directory(
            os.path.join(tempfile.gettempdir(), self.temp_entity))  
        
        if self.subfield == 'model':
            self.make_maya_model(force=False)
            self.make_thumbnail()            
            self.make_studio_model()
            self.make_model_usd()
            self.make_maya()
            self.make_manifest()
            
        if self.subfield == 'uv':
            self.make_maya_model(force=False)
            self.make_thumbnail()         
            self.make_studio_uv()
            self.make_uv_usd()
            self.make_maya()
            self.make_manifest()            
            
        if self.subfield == 'surface':
            self.make_maya_model(force=False)
            self.make_thumbnail()        
            self.make_source_images()
            self.make_studio_surface()            
            self.make_surface_usd()
            self.make_surface_maya()
            self.make_manifest()            
                     
        if self.subfield == 'puppet':
            self.make_maya_model(force=False)
            self.make_thumbnail()
            self.make_studio_puppet()
            # self.make_source_images()                     
            self.make_puppet_usd()            
            self.make_maya()
            self.make_manifest()
            
        if self.subfield == 'usd':
            self.make_composition_usd(kwargs['composition'], force=False)
            self.make_thumbnail()
            self.make_manifest()
            
        for key in self.data:
            if not self.data[key]:
                continue       
            for each in self.data[key]:
                if not each:
                    continue                
                # if not os.path.exists(each):
                #    continue            
                os.utime(each, (self.time_stamp, self.time_stamp))

    def release(self):  
        result = self.move_to_publish()        
        if not result:
            return        
        date = time.strftime('%Y/%d/%B - %I/%M/%S/%p', time.gmtime(self.time_stamp))
        kwargs = {
            'caption': {
                'value': self.caption,
                'order': 0
                },
            'version': {
                'value': self.version,
                'order': 1
                },
            'subfield': {
                'value': self.subfield,
                'order': 2
                },
            'type': {
                'value': self.type,
                'order': 3
                },
            'tag': {
                'value': self.tag,
                'order': 4
                },
            'date': {
                'value': date,
                'order': 5
                },
            'location': {
                'value': self.publish_path,
                'order': 6
                }
            } 
        self.dbs.create(kwargs)
    
    def move_to_publish(self):   
        temp_pack_path = os.path.join(
            tempfile.gettempdir(), self.temp_entity)   
        self.make_directory(self.publish_path)  
        for key in self.data:
            if not self.data[key]:
                continue
            for each in self.data[key]:
                if not each:
                    continue
                path = each.replace(temp_pack_path, self.publish_path)
                if os.path.isdir(each):
                    if not os.path.isdir(path):
                        os.makedirs(path)
                        self.set_time_stamp(path)
                if os.path.isfile(each):                 
                    if not os.path.isdir(os.path.dirname(path)):
                        os.makedirs(os.path.dirname(path))
                    try:            
                        shutil.copy2(each, path)
                    except Exception as IOError:
                        print IOError
                        return False
        return True

    def make_maya_model(self, force=False):
        '''
            import time
            from studio_usd_pipe.core import asset
            reload(asset)        
            asset = asset.Asset(subfield='model')        
            bundle = {
                'source_file': '/venture/shows/my_hero/dumps/batman_finB.ma',
                'caption': 'batman',
                'version': '0.0.0',
                'thumbnail': '/local/references/images/btas_batmodel_03.jpg',
                'type': 'interactive',
                'tag': 'character',
                'description': 'test publish',
                'time_stamp': time.time()
                }        
            asset.make_maya_model(bundle)        
        '''
        inputs = {
            self.asset_ids[0]: self.entity,
            self.asset_ids[1]: self.caption,
            self.asset_ids[2]: self.type,
            self.asset_ids[3]: self.tag,
            self.asset_ids[4]: self.version,
            self.asset_ids[5]: self.time_stamp,
            self.asset_ids[6]: self.publish_path,
            self.asset_ids[7]: self.description,
            'node': 'model',
            'world': 'world'
            }
        self.mpack.create_model(inputs, force=force)  
         
    def make_thumbnail(self):
        inputs = {
            'standalone': self.standalone,
            'output_directory': self.temp_pack_path,
            'caption': self.caption,
            'thumbnail': self.thumbnail,
            'time_stamp': self.time_stamp,
            'width': 768,
            'height': 768,
            'force': True
            } 
        thumbnail = self.mpack.create_thumbnail(inputs)
        self.data['thumbnail'] = [thumbnail]    
                         
    def make_maya(self):
        inputs = {
            'node': 'model',
            'output_directory': self.temp_pack_path,
            'caption': self.caption,
            'time_stamp': self.time_stamp,
            'force': True
            }        
        maya_file = self.mpack.create_maya(inputs)
        self.data['maya_file'] = [maya_file]
        
    def make_surface_maya(self):
        inputs = {
            'node': 'model',
            'output_directory': self.temp_pack_path,
            'caption': self.caption,
            'time_stamp': self.time_stamp,
            'force': True
            }        
        maya_file = self.mpack.create_surface_maya(inputs)
        self.data['maya_file'] = [maya_file]        
        
    def make_studio_model(self):
        inputs = {
            'node': 'model',
            'output_directory': self.temp_pack_path,
            'caption': self.caption,
            'time_stamp': self.time_stamp,
            'force': True
            }       
        studio_model = self.mpack.create_studio_model(inputs)
        self.data['studio_model'] = [studio_model]    
 
    def make_studio_uv(self):
        inputs = {
            'node': 'model',
            'output_directory': self.temp_pack_path,
            'caption': self.caption,
            'time_stamp': self.time_stamp,
            'force': True
            }       
        studio_uv = self.mpack.create_studio_uv(inputs)
        self.data['studio_uv'] = [studio_uv]
    
    def make_studio_puppet(self):
        self.data['studio_puppet'] = None
                
    def make_source_images(self): 
        inputs = {
            'node': 'model',
            'output_directory': self.temp_pack_path,
            'publish_directory': self.publish_path,
            'caption': self.caption,
            'time_stamp': self.time_stamp,
            'force': False
            }
        souce_data, source_images = self.mpack.create_source_images(inputs)
        self.data['source_image_data'] = [souce_data]
        self.data['source_images'] = source_images
        self.data['source_images_directory'] = [os.path.join(
            self.temp_pack_path, 'source_images')]   
                
    def make_studio_surface(self):
        inputs = {
            'node': 'model',
            'output_directory': self.temp_pack_path,
            'caption': self.caption,
            'time_stamp': self.time_stamp,
            'force': True
            }       
        studio_surface = self.mpack.create_studio_surface(inputs)
        self.data['studio_surface'] = [studio_surface]     
 
    def make_model_usd(self):
        inputs = {
            'node': 'model',
            'output_directory': self.temp_pack_path,
            'caption': self.caption,
            'time_stamp': self.time_stamp,
            'force': True
            }
        usd = self.mpack.create_model_usd(inputs, asset_ids=self.asset_ids)
        self.data['usd_model'] = [usd]    
        
    def make_uv_usd(self):   
        inputs = {
            'node': 'model',
            'output_directory': self.temp_pack_path,
            'caption': self.caption,
            'time_stamp': self.time_stamp,
            'force': True
            }        
        usd = self.mpack.create_uv_usd(inputs, asset_ids=self.asset_ids)
        self.data['usd_uv'] = [usd]
        
    def make_surface_usd(self):
        inputs = {
            'node': 'model',
            'output_directory': self.temp_pack_path,
            'caption': self.caption,
            'time_stamp': self.time_stamp,
            'force': True
            }        
        usd = self.mpack.create_surface_usd(inputs, asset_ids=self.asset_ids)
        self.data['usd_surface'] = [usd]
        
    def make_puppet_usd(self):
        self.data['usd_puppet'] = None
    
    def make_manifest(self):
        source_images = None
        if 'source_images' in self.data:
            source_images = self.data['source_images']
        
        maya_file, studio_format, usd, thumbnail = [None], [None], [None], [None]

        if 'maya_file' in self.data:
            maya_data = self.data['maya_file']
            
            if maya_data:
                maya_dirname = os.path.basename(maya_data[0])
                maya_file = [os.path.join(self.publish_path, maya_dirname)]
            else:
                maya_file = None
            
        if 'studio_%s' % self.subfield in self.data:
            studio_data = self.data['studio_%s' % self.subfield]
            if studio_data:
                studio_dirname = os.path.basename(studio_data[0])
                studio_format = [os.path.join(self.publish_path, studio_dirname)]
            else:
                studio_format = None
        
        if 'usd_%s' % self.subfield in self.data:
            usd_data = self.data['usd_%s' % self.subfield]
            if usd_data:
                usd_dirname = os.path.basename(usd_data[0])
                usd = [os.path.join(self.publish_path, usd_dirname)]
            else:
                usd = None
            
        if 'thumbnail' in self.data: 
            thumbnail_data = self.data['thumbnail']
            if thumbnail_data:
                thumbnail_dirname = os.path.basename(thumbnail_data[0])
                thumbnail = [os.path.join(self.publish_path, thumbnail_dirname)]
            else:
                thumbnail = None
                      
        inputs = {
            'output_directory': self.temp_pack_path,
            'location': self.publish_path,
            'caption': self.caption,
            'version': self.version,
            'type': self.type,
            'tag': self.tag,
            'description': self.description,
            'time_stamp': self.time_stamp,
            'source_file': self.source_maya,
            'maya': maya_file,
            'studio_format': studio_format,
            'usd': usd,
            'thumbnail': thumbnail,
            'source_images': source_images,
            'force': True,
            'subfield': self.subfield
            }
        
        print '#' * 50
        print json.dumps(inputs, indent=4)
        print '#' * 50
        
        mainfest = self.mpack.create_manifest(inputs)
        self.data['mainfest'] = [mainfest]
        
    def make_composition_usd(self, composition_data, force=False):
        self.data['composition'] = None      
            
    def make_directory(self, directory):
        if os.path.isdir(directory):
            self.reomve_dirname(directory)            
        os.makedirs(directory, 0755)
        self.set_time_stamp(directory)
        return directory
        
    def reomve_dirname(self, dirname):
        if not os.path.isdir(dirname):
            return
        os.chmod(dirname, 0777)
        try:
            shutil.rmtree(dirname)
        except Exception as OSError:
            print OSError

    def set_time_stamp(self, path):
        if not os.path.exists(path):
            return
        os.utime(path, (self.time_stamp, self.time_stamp)) 

