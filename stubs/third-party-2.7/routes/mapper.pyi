# Stubs for routes.mapper (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

COLLECTION_ACTIONS = ... # type: Any
MEMBER_ACTIONS = ... # type: Any

def strip_slashes(name): ...

class SubMapperParent:
    def submapper(self, **kargs): ...
    def collection(self, collection_name, resource_name, path_prefix=None, member_prefix='', controller=None, collection_actions=..., member_actions=..., member_options=None, **kwargs): ...

class SubMapper(SubMapperParent):
    kwargs = ... # type: Any
    obj = ... # type: Any
    collection_name = ... # type: Any
    member = ... # type: Any
    resource_name = ... # type: Any
    formatted = ... # type: Any
    def __init__(self, obj, resource_name=None, collection_name=None, actions=None, formatted=None, **kwargs): ...
    def connect(self, *args, **kwargs): ...
    def link(self, rel=None, name=None, action=None, method='', formatted=None, **kwargs): ...
    def new(self, **kwargs): ...
    def edit(self, **kwargs): ...
    def action(self, name=None, action=None, method='', formatted=None, **kwargs): ...
    def index(self, name=None, **kwargs): ...
    def show(self, name=None, **kwargs): ...
    def create(self, **kwargs): ...
    def update(self, **kwargs): ...
    def delete(self, **kwargs): ...
    def add_actions(self, actions): ...
    def __enter__(self): ...
    def __exit__(self, type, value, tb): ...

class Mapper(SubMapperParent):
    matchlist = ... # type: Any
    maxkeys = ... # type: Any
    minkeys = ... # type: Any
    urlcache = ... # type: Any
    prefix = ... # type: Any
    req_data = ... # type: Any
    directory = ... # type: Any
    always_scan = ... # type: Any
    controller_scan = ... # type: Any
    debug = ... # type: Any
    append_slash = ... # type: Any
    sub_domains = ... # type: Any
    sub_domains_ignore = ... # type: Any
    domain_match = ... # type: Any
    explicit = ... # type: Any
    encoding = ... # type: Any
    decode_errors = ... # type: Any
    hardcode_names = ... # type: Any
    minimization = ... # type: Any
    create_regs_lock = ... # type: Any
    def __init__(self, controller_scan=..., directory=None, always_scan=False, register=True, explicit=True): ...
    environ = ... # type: Any
    def extend(self, routes, path_prefix=''): ...
    def make_route(self, *args, **kargs): ...
    def connect(self, *args, **kargs): ...
    def create_regs(self, *args, **kwargs): ...
    def match(self, url=None, environ=None): ...
    def routematch(self, url=None, environ=None): ...
    obj = ... # type: Any
    def generate(self, *args, **kargs): ...
    def resource(self, member_name, collection_name, **kwargs): ...
    def redirect(self, match_path, destination_path, *args, **kwargs): ...
