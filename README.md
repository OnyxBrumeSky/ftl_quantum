# ftl_quantum
# small project to learn quantum programming 

# To see plot in jupyter use : 
%matplotlib inline

# To remove virtual env : 
rm -rf qiskit_env

# To connect to IBM using API KEY do :
from qiskit_ibm_runtime import QiskitRuntimeService
QiskitRuntimeService.save_account(token="API_TOKEN", overwrite=True)
# Private API key is not shown here and should be unique and never shared
