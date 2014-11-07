# GLOBAL CONFIGURATION

# ADD A FUNCTION THAT RANDOMLY SELECTS A STRING FROM A LIST
# AND THEN MAKES IT THE WEBSITE NAME
WEBSITE_NAME = "Michael Anzuoni's cool home on the web!"
DEBUG = True

# ARTICLE AND PAGE CONFIGURATION

ARTICLE_DIR = './articles/'
PAGES_DIR = './pages/'

# NAVBAR CONFIGURATION
# Add navbar links with dict(title="Title", url="URL)

NAV = [dict(title="C V", url="/resume"), dict(title="c0des", url="https://github.com/yolesaber")]

# SECURITY CONFIGURATION

SECRET_KEY = 'SECRET_KEY'

# Accept all standard markdown file extensions.

EXTENSIONS = ('.markdown', '.mdown', '.mkdn', '.md', '.mkd', '.mdwn', '.mdtxt', '.mdtext', '.text')
