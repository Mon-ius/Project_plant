from collections import namedtuple

profileAttr = ['realname', 'phonenum', 'college', 'status', 'birth']
profilebase = namedtuple('profilebase', profileAttr)

extraAttr = ['experience', 'award', 'file']
extrabase = namedtuple('extrabase', extraAttr)

projectsAttr = ['pid','pname','file']
projectsbase = namedtuple('projectsbase', projectsAttr)

userAttr = ['admin', 'name', 'email', 'passwd']
userbase = namedtuple('userbase', userAttr)
