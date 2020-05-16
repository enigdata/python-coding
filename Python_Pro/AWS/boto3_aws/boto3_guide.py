import boto3 

#s3_client = boto3.client('s3') #lower-level API calls
s3_resource = boto3.resource('s3')

import uuid 

def create_bucket_name(bucket_prefix):
    return ''.join([bucket_prefix, str(uuid.uuid4())])

print(create_bucket_name('test_name'))

def create_bucket(bucket_prefix, s3_connection):
    session = boto3.session.Session()
    current_region = session.region_name
    bucket_name = create_bucket_name(bucket_prefix)
    if current_region == 'us-east-1':
        bucket_response = s3_connection.create_bucket(
        Bucket = bucket_name)
    else:
        bucket_response = s3_connection.create_bucket(
            Bucket = bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': current_region
            }
        )
    print(bucket_name, current_region)
    #print(bucket_response)
    return bucket_name, bucket_response

first_bucket_name, first_response = create_bucket('firstbucket', s3_resource.meta.client)
#firstbucketb2eee48c-3645-4ec5-ad55-5e834b80edbe 

second_bucket_name, second_response = create_bucket('secondbucket', s3_resource.meta.client)
#secondbucketc5cf059d-bd91-4906-b93d-8cf3e0514096

#### Naming Files 
def create_temp_file(size, file_name, file_content):
    random_file_name = ''.join([str(uuid.uuid4().hex[:6]), file_name])
    with open(random_file_name, 'w') as f:
        f.write(str(file_content)*size)
    return random_file_name

first_file_name = create_temp_file(300, 'firstfile.txt', 'f')
print(first_file_name)