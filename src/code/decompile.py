import paths
import bashutils

import warnings
warnings.filterwarnings("ignore")

class Decompiler():
    """
    Purpose:

    Variables:

    I/O:
        Number of Parameters Taken: 2
        Input .apk file -> It is the .apk file which needs to be decompiled.
        Output Directory -> It is the output directory which will contain the decompiled code. 
    """

    def __init__(self,input_file,output_file):
        self.path = paths.Paths()
        self.name = input_file
        self.input = self.path.apk_dir + input_file + '.apk'
        self.output = self.path.output_dir+output_file


    def extract_to_jar(self):
        command = self.path.dare_dir+'dare -o -e -p -d '+self.output+' '+self.input
        bashutils.execute(command)
        command = 'jar cvf '+self.path.output+'classes_'+self.name+'.jar -C '+self.output+'/retargeted/'+self.name+'/ .'
        bashutils.execute(command)

    def decompile(self):
        command = 'java -jar '+self.path.decompiler_dir+'procyon-decompiler.jar -jar '+self.path.output_dir+'classes_'+self.name+'.jar -o '+self.output+'/decompiled/'
        bashutils.execute(command)

class StaticAnalyzer():
    def GetHardcodedCert(files):
    print "[INFO] Getting Hardcoded Certificates"
        cert=[]
        cert = search_file_level(["cer","pem","cert","crt","pub","key","pfx","p12"]);
        return cert
        
    return re.sub(RE_XML_ILLEGAL, "?", dat)

    def HashGen(APP_PATH):
    print "[INFO] Generating Hashes"
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()
    BLOCKSIZE = 65536
    with io.open(APP_PATH, mode='rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            sha1.update(buf)
            sha256.update(buf)
            buf = afile.read(BLOCKSIZE)
    sha1val = sha1.hexdigest()
    sha256val=sha256.hexdigest()
    return sha1val, sha256val

    def FileSize(APP_PATH): 
        return round(float(os.path.getsize(APP_PATH)) / (1024 * 1024), 2 )

if __name__ == "__main__":
    input_file = raw_input('Enter the name of the .apk file from input directory\n')
    output_file = raw_input('Enter the name of the directory you wish to save your output\n')
    print('Starting...!')
    decompiler = Decompiler(input_file,output_file)
    decompiler.extract_to_jar()
    decompiler.decompile()
    print('Done!')