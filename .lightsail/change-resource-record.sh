#!/bin/bash

# setting the subdomain www.dr-data-dude.com
#aws route53 change-resource-record-sets --hosted-zone-id Z02311982Y816PZ0D3ZXL --change-batch file://change-resource-record-sets.json
# setting the apex domain dr-data-dude.com
#aws route53 change-resource-record-sets --hosted-zone-id Z02311982Y816PZ0D3ZXL --change-batch file://change-resource-record-sets-apex.json