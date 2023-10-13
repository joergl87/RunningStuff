import xml.etree.ElementTree as ET
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Defining namespaces for better readability and accurate tag location
namespaces = {
    '': 'http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2'
    # You can add other namespaces here if needed
}
# Registering namespaces
for prefix, uri in namespaces.items():
    ET.register_namespace(prefix, uri)

tree_master = ET.parse('../Aktivitäten Export/EmptyActivityTemplate.tcx')
root_master = tree_master.getroot()
activities_master = root_master.find('./Activities', namespaces)

# Path where your tcx files are stored
path_to_tcx_files = '../Aktivitäten Export/'

# Iterating over all tcx files in the specified directory
for filename in os.listdir(path_to_tcx_files):
    if filename.endswith('.tcx'):
        tree_current = ET.parse(os.path.join(path_to_tcx_files, filename))
        root_current = tree_current.getroot()
        activities_current = root_current.find('.//Activities', namespaces)

        # Appending each Activity node to the master xml file
        for activity in activities_current:
            activities_master.append(activity)

# Save the merged XML
tree_master.write('merged.tcx', encoding='utf-8', xml_declaration=True)