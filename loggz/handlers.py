import gzip
import logging
import logging.handlers
import os
import shutil

class GzipRotatingFileHandler(logging.handlers.RotatingFileHandler):
    
    def doRollover(self):
        """
        Do a rollover, as described in __init__().
        """
        
        if self.stream:
            self.stream.close()
            self.stream = None
            
        if self.backupCount > 0:
            
            # Compressed files
            for i in range(self.backupCount - 1, 1, -1):
                
                sfn = self.rotation_filename(
                    "%s.%d.gz" % (self.baseFilename, i))
                dfn = self.rotation_filename(
                    "%s.%d.gz" % (self.baseFilename, i + 1))
                
                if os.path.exists(sfn):
                    
                    if os.path.exists(dfn):
                        os.remove(dfn)
                        
                    os.rename(sfn, dfn)
                    
            # First backup (not compressed)                
            sfn = self.rotation_filename(
                "%s.1" % self.baseFilename)
            dfn = self.rotation_filename(
                "%s.2.gz" % self.baseFilename)
            
            if os.path.exists(sfn):
                
                if os.path.exists(dfn):
                    os.remove(dfn)
                
                dst = gzip.open(dfn, "wb")
                src = open(sfn, "rb")
                shutil.copyfileobj(src, dst)
                dst.close()
                src.close()
                
                os.unlink(sfn)
                    
            dfn = self.rotation_filename(self.baseFilename + ".1")
            
            if os.path.exists(dfn):
                os.remove(dfn)
            
            self.rotate(self.baseFilename, dfn)
        
        if not self.delay:
            self.stream = self._open()
 