#az extension add --name communication
$rg="az-communication-service-rg"

$com_name= az communication list --resource-group $rg --query "[0].name" -o tsv

#az communication list-key --name $com_name --resource-group $rg 
$connection_string=az communication list-key --name $com_name --resource-group $rg --query "primaryConnectionString" -o tsv


# create identity
#az communication identity user create --connection-string $connection_string
# create token
#az communication identity token issue --scope chat --user $user_id --connection-string $connection_string

# create identity and token
az communication identity token issue --scope chat --connection-string $connection_string
