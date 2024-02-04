import subprocess
import json
def validate(path):
    p = subprocess.Popen(["terraform", "validate -json"], cwd=path, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, errors = p.communicate()
    Errors = str(errors)
    if Errors == "b''":
        print("Terraform validation is successful.")
    else:
        Errors = errors.decode()
        print("Terraform validation failed.")
        print(Errors)
'''
    if p.returncode == 0:
        output_json = json.loads(output)
        print(json.dumps(output_json, indent=4))  
    else:
        print("Validation errors:")
        print(errors.decode("utf-8"))
'''
