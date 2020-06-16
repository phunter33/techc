Table of contents
=================

<!--ts-->
   * [Challenge1](#challenge1)
      * [Description](#challenge1-desc)
      * [Output](#challenge1-output)   
   * [Challenge2](#challenge2)
      * [Description](#challenge2-desc)
      * [Output](#challenge2-output)   
   * [Challenge3](#challenge3)
      * [Description](#challenge3-desc)
      * [Output](#challenge3-output)   
<!--te-->

Challenge1
=====  

challenge1-desc
----- 

A 3-tier environment is a common setup. Use a tool of your choosing/familiarity create these resources. 

challenge1-output
----- 

    IAC tech used for the above is Cloudformation.

    AWS services used :

    AWS::EC2
    AWS::ElasticLoadBalancing::LoadBalancer
    AWS::AutoScaling::AutoScalingGroup
    AWS::EC2::SecurityGroup
    AWS::EC2::VPC
    AWS::S3::Bucket
    AWS::RDS::DBInstance
    AWS::SNS
    AWS::CloudFront::Distribution
 
Challenge2
=====  

challenge2-desc
----- 

    Summary
    We need to write code that will query the meta data of an instance within aws and provide a json formatted output. The choice of language and implementation is up to you.

 
    Bonus Points
    The code allows for a particular data key to be retrieved individually

        Hints : Aws Documentation
                Azure Documentation
                Google Documentation

challenge2-output
----- 
There are 2 ways to fetch the metadata of EC2 instance 
 - aws-cli commands from outside the instance

```bash
>> aws ec2 describe-instance-attribute --instance-id <instanceid>

To fetch particular value 

>> aws ec2 describe-instance-attribute --instance-id i-0d6c0b2dd3c4baae7 | jq .InstanceType.Value
```

- API call from inside the instance

```bash
>> python ./challenge2/getec2metainfo.py
```
    

Challenge3
=====  

challenge3-desc
----- 
    We have a nested object, we would like a function that you pass in the object and a key and get back the value. How this is implemented is up to you.

 
    Example Inputs
    object = {“a”:{“b”:{“c”:”d”}}}
    key = a/b/c
 
    object = {“x”:{“y”:{“z”:”a”}}}
    key = x/y/z
    value = a

challenge3-output
----- 

```bash
USAGE : sh ./challenge3/objectparser.sh  help

     2 params Required  

     1 - inputString 
     2 - keyName to find 

    example 1 : 
               sh ./challenge3/objectparser.sh  {“a”:{“b”:{“c”:”d”}}} a/b/c >> Output : d  
    
    example 2 : 
               sh ./challenge3/objectparser.sh {“x”:{“y”:{“z”:”a”}}} x/y/z  >> Output : a  
 
```
    
