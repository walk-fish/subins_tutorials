
import os
import copy
import shutil

from studio_usd_pipe import resource
from studio_usd_pipe.core import common
from studio_usd_pipe.core import database
from studio_usd_pipe.api import studioEnviron


class Pipe(object): # pipe == asset or shot
    
    def __init__(self, current_show, current_pipe):
        self.current_show = current_show
        self.current_pipe = current_pipe
        self.show_path = self.get_show_path()
        self.pipe_inputs = resource.getPipeData()['pipe'][self.current_pipe]

    def get_show_path(self):
        environ = studioEnviron.Environ(self.current_show)
        show_path, valid = environ.get_environ_value('SHOW_PATH')
        return show_path
    
    def get_composition_subfields(self):
        composition_subfields = []
        valid_subfields = ['model', 'uv', 'shader']
        for subfield in self.pipe_inputs['subfield']['values']:            
            if subfield not in valid_subfields:
                continue            
            composition_subfields.append(subfield)
        return composition_subfields
    
    def get_casting_subfields(self):
        casting_subfields = []
        valid_subfields = ['puppet', 'composition']
        for subfield in self.pipe_inputs['subfield']['values']:            
            if subfield not in valid_subfields:
                continue            
            casting_subfields.append(subfield)
        return casting_subfields    
    
        
    def get(self):
        dbs = database.DataBase(self.current_show, self.current_pipe)   
        data = dbs.get()        
        db_data = {}
        for table, contents in data.items(): 
            if contents['caption'] not in db_data:
                db_data.setdefault(contents['caption'], {})
            if contents['subfield'] not in db_data[contents['caption']]:
                db_data[contents['caption']].setdefault(contents['subfield'], {}) 
            
            updated_data = copy.deepcopy(contents)
            updated_data['table'] = table
            
            db_data[contents['caption']][contents['subfield']].setdefault(
                contents['version'], updated_data)
        return db_data
    
    def get_table_data(self):
        dbs = database.DataBase(self.current_show, self.current_pipe)   
        data = dbs.get()
        return data
    
    def get_pipes(self):
        db_data = self.get()        
        return db_data.keys()

    def get_subfields(self, caption, db_data=None):
        if not db_data:
            db_data = self.get()
        subfield_data = {}
        if caption in db_data:
            subfield_data = db_data[caption]
        return subfield_data   
    
    def get_specific_captions_key(self, key, db_data=None):
        if not db_data:
            db_data = self.get()
        key_data = {}
        for sasset, subfields in db_data.items():
            for subfield in subfields:
                for version in subfields[subfield]:
                    if key not in subfields[subfield][version]:
                        continue
                    specific_key = subfields[subfield][version][key]
                    if sasset not in key_data:
                        key_data.setdefault(sasset, [])
                    if specific_key in key_data[sasset]:
                        continue
                    key_data.setdefault(sasset, []).append(specific_key)
        return key_data
    
    def get_caption_type(self, db_data=None):
        if not db_data:
            db_data = self.get()        
        type_data = self.get_specific_captions_key('type', db_data=db_data)
        return type_data    
    
    def get_caption_tag(self, db_data=None):
        if not db_data:
            db_data = self.get()        
        type_data = self.get_specific_captions_key('tag', db_data=db_data)
        return type_data        
    
    def get_versions_data(self, caption, subfield, db_data=None):
        if not db_data:
            db_data = self.get()
        subfield_data = self.get_subfields(caption, db_data=db_data)
        version_data = {}
        for k, v in subfield_data.items():    
            if k != subfield:
                continue        
            version_data.update(v)        
        return version_data
    
    def get_version_data(self, caption, subfield, version, db_data=None):
        if not db_data:
            db_data = self.get()        
        versions_data = self.get_versions_data(caption, subfield, db_data=db_data)
        if version not in versions_data:
            return
        final_data = self.get_more_data(caption, subfield, version)
        final_data.update(versions_data[version])
        return final_data
    
    def get_versions(self, caption, subfield, db_data=None):
        if not db_data:
            db_data = self.get()        
        version_data = self.get_versions_data(caption, subfield, db_data=db_data)
        versions = common.set_version_order(version_data.keys())
        return versions  
    
    def get_latest_version(self, caption, subfield, db_data=None):
        if not db_data:
            db_data = self.get()          
        versions = self.get_versions(caption, subfield, db_data=db_data)
        if not versions:
            return None
        return versions[0]          
    
    def get_next_version(self, caption, index, subfield, latest_version=None):
        '''
            index 0, 1, 2 = MAJOR0, MINOR, PATCH
        '''
        if not latest_version:
            latest_version = self.get_latest_version(caption, subfield)
        if not latest_version:
            return '0.0.0'
        n_version = common.get_next_version(caption, index, subfield, latest_version)
        return n_version
        
    def get_dependencies(self, caption, db_data=None):
        if not db_data:
            db_data = self.get()        
        dependencies = self.get_versions(
            caption, 'model', db_data=db_data)
        dependencies = ['None'] + dependencies
        return dependencies
         
    def get_more_data(self, caption, subfield, version):
        '''
            add manifest data as well
        '''
        manifest_path = os.path.join(
            self.show_path,
            self.current_pipe,
            caption,
            subfield,
            version,
            '{}.manifest'.format(caption)
            )
        sorted_data = {}
        if not os.path.isfile(manifest_path):
            return sorted_data
        data = resource.getInputData(manifest_path)
        sorted_data = copy.deepcopy(data)
        extrude = ['caption', 'tag', 'user', 'modified', 'location', 'type']
        for each in data:
            if each not in extrude:
                continue
            sorted_data.pop(each)
        return sorted_data
    
    def remove(self, table, pipe_path):
        dbs = database.DataBase(self.current_show, self.current_pipe)   
        dbs.delete_table(table)
        if os.path.isdir(pipe_path):
            shutil.rmtree(pipe_path)
            
    def get_castingsheet_data(self):
        castingsheet_path = resource.getSpecificPreset(self.show_path, 'castingsheet')
        casting_data = {}
        if not os.path.isfile(castingsheet_path):
            return casting_data
        casting_data = resource.getInputData(castingsheet_path)
        return casting_data
    
    def get_castingsheet_captions(self):
        casting_data = self.get_castingsheet_data()        
        captions = []        
        for toplevel, sublevels in casting_data.items():
            for sublevel in sublevels:
                captions.append('%s|%s'%(toplevel, sublevel))
        captions = sorted(captions)
        return captions                
                             
        