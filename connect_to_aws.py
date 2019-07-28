# Reading credentials in, best practice is to use IAM role

def connect(file,region):
	keys = []
	with open(file,'r') as f:
	    csv_reader = csv.DictReader(f)
	    for row in csv_reader:
	        keys = list(row.values())
	        
	# Credentials & Region
	access_key = keys[0]
	secret_key = keys[1]
	region = region

	ec2_client = boto3.client(
    'ec2',
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name=region
	)