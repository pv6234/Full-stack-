from pyDatalog import pyDatalog
pyDatalog.create_atoms('parent,male,female,son,daughter,X,Y,Z')
+male('adam')
+female('anne')
+female('barney')
+male('james')
+parent('barney','adam')
+parent('james','anne')
