import xml.etree.ElementTree as ET

class MetadataValidator:
    REQUIRED_FIELDS = ['Title', 'Confidence', 'Tags', 'ExampleInput', 'ExampleOutput', 'Creator']

    def __init__(self, xml_file):
        self.xml_file = xml_file

    def validate(self):
        tree = ET.parse(self.xml_file)
        root = tree.getroot()

        errors = []

        for field in self.REQUIRED_FIELDS:
            if root.find(field) is None:
                errors.append(f"Missing required field: {field}")
            else:
                value = root.find(field).text
                if value is None or value.strip() == '':
                    errors.append(f"Field '{field}' is empty.")

        return errors

if __name__ == '__main__':
    validator = MetadataValidator('path/to/prompt_file.xml')
    validation_errors = validator.validate()

    if validation_errors:
        for error in validation_errors:
            print(error)
    else:
        print('All required fields are present and valid.')
