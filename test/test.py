def make(i):
    fold = 'test_0'+ str(i)
    os.makedirs(fold)
    for filename in ['begin','middle','final']:
        content = fold+'_'+filename
        file= open(fold+'/'+content+'.doc','w')
        file.write(content)
        file.close()
for i in range(1,10):
    make(i)