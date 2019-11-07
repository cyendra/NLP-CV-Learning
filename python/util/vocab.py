# encode='utf-8'
import time
import pickle

class Vocab:
    def __init__(self, name='vocab', version='v1.0', file_path=''):
        self._vocab = {'<EMP>' : 0, '<UNK>' : 1, '<EOP>' : 2
                    , '<CLS>' : 3, '<SEP>' : 4, '<PAD>' : 5
                    , '<MASK>' : 6, '<EOD>' : 7, '<S>' : 8
                    , '</S>' : 9}
        self._count = 100
        
        create_date = time.strftime("%Y.%m.%d %H:%M:%S", time.localtime()) 
        self._meta = {'name' : name, 'version' : version
                        , 'create_date' : create_date
                        , 'update_date' : create_date
                        , 'save_date' : create_date
                        , 'save_count' : 0
                        , 'file_path' : file_path}
    
    def set_name(self, name=''):
        if len(name) > 0:
            self._meta['name'] = name
    
    def set_version(self, version=''):
        if len(version) > 0:
            self._meta['version'] = version
    
    def load(self, file_path=''):
        if len(file_path) == 0:
            file_path = self._meta['file_path']
        if len(file_path) == 0:
            raise Exception("file_path is empty!")
        with open(file_path, 'rb') as f:
            data = pickle.load(f)
            self._vocab = data._vocab
            self._meta = data._meta
            self._count = data._count
    
    def save(self, file_path=''):
        if len(file_path) == 0:
            file_path = self._meta['file_path']
        if len(file_path) == 0:
            raise Exception("file_path is empty!")
        self._meta['file_path'] = file_path
        save_date = time.strftime("%Y.%m.%d %H:%M:%S", time.localtime()) 
        self._meta['save_date'] = save_date
        self._meta['save_count'] = self._meta['save_count'] + 1
        with open(file_path, 'wb') as f:
            pickle.dump(self, f)
    
    def refresh(self, need_refresh=True):
        if need_refresh:
            update_date = time.strftime("%Y.%m.%d %H:%M:%S", time.localtime()) 
            self._meta['update_date'] = update_date

    def add(self, word, need_refresh=True):
        if word not in self._vocab:
            self._vocab[word] = self._count
            self._count += 1
            self.refresh(need_refresh)
    
    def extend(self, dic, need_refresh=True):
        for x in dic:
            if isinstance(x, str):
                self.add(x, need_refresh=False)
        self.refresh(need_refresh)
    
    def meta(self):
        for key in self._meta.keys():
            print(key, ':', self._meta[key])
        print('size : ', self._count)