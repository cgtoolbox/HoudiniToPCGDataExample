import json
import sys

import unreal
UnrealEditorSubsystem = unreal.get_editor_subsystem(unreal.UnrealEditorSubsystem)

json_path = sys.argv[1]

with open(json_path, 'r') as f:
    geo_data = json.load(f)

# Get point positions
positions = geo_data["positions"]

# Float attributes
float_struct_bp = geo_data["float_attribs_bp_class"]
float_struct_bp = unreal.load_asset(float_struct_bp)

float_attribs = []
for float_attr_name, float_attr_infos in geo_data["float_attribs"].items():

    obj = unreal.new_object(float_struct_bp)
    obj.set_editor_property("AttribName", float_attr_name)
    obj.set_editor_property("AttribSize", float_attr_infos["size"])
    obj.set_editor_property("AttribValues", float_attr_infos["attrib_values"])
    float_attribs.append(obj)

# String attributes
string_struct_bp = geo_data["string_attribs_bp_class"]
string_struct_bp = unreal.load_asset(string_struct_bp)

string_attribs = []
for string_attr_name, string_attr_infos in geo_data["string_attribs"].items():

    obj = unreal.new_object(string_struct_bp)
    obj.set_editor_property("AttribName", string_attr_name)
    obj.set_editor_property("AttribValues", string_attr_infos["attrib_values"])
    obj.set_editor_property("IsSoftPath", string_attr_infos["is_soft_path"])
    string_attribs.append(obj)

# Int attributes
int_struct_bp = geo_data["int_attribs_bp_class"]
int_struct_bp = unreal.load_asset(int_struct_bp)

int_attribs = []
for int_attr_name, int_attr_infos in geo_data["int_attribs"].items():

    obj = unreal.new_object(int_struct_bp)
    obj.set_editor_property("AttribName", int_attr_name)
    obj.set_editor_property("AttribValues", int_attr_infos["attrib_values"])
    int_attribs.append(obj)

# Execute the blueprint in charge of the PCG data asset.
bp_class = unreal.load_object(None, geo_data["create_pcg_data_bp_class"])
bp_cdo = unreal.get_default_object(bp_class) 

bp_cdo.call_method("Create PCGData", (geo_data["asset_path"], geo_data["asset_name"], positions, float_attribs, string_attribs, int_attribs))
