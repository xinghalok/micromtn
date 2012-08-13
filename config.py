# GLOBAL CONFIGURATION

# ADD A FUNCTION THAT RANDOMLY SELECTS A STRING FROM A LIST
# AND THEN MAKES IT THE WEBSITE NAME
WEBSITE_NAME = 'mea'
DEBUG = True

# ARTICLE AND PAGE CONFIGURATION

ARTICLE_DIR = '/var/www/micromtn/articles/'
PAGES_DIR = '/var/www/micromtn/pages/'

# NAVBAR CONFIGURATION
# Add navbar links with dict(title="Title", url="URL)

NAV = [dict(title='Home', url='/'), dict(title="Resume", url="/resume"), dict(title="Code", url="https://github.com/yolesaber")]

# SECURITY CONFIGURATION

SECRET_KEY = 'SECRET_KEY'

# Accept all standard markdown file extensions.

EXTENSIONS = ('.markdown', '.mdown', '.mkdn', '.md', '.mkd', '.mdwn', '.mdtxt', '.mdtext', '.text')
