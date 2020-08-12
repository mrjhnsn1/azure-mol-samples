#!/bin/bash
# need to mount ssh keys for this scrpit to work.
# docker run -it -v ${HOME}/.ssh:/root/.ssh mcr.microsoft.com/azure-cli:ro

#az vm create --name $VMName --resource-group $resourceGroup --admin-username $admin --authentication-type ssh --boot-diagnostics-storage $bootDiagStorage --custom-data $customData --image $image --location $location --nics $nics --ssh-key-value $keyFile --subscription $subs --secrets $vm_secret

#   --generate-ssh-keys \

az vm create \
   --resource-group azuremolchapter4 \
   --name storagevm \
   --image UbuntuLTS \
   --admin-username azuremol \
   --authentication-type ssh \
   --ssh-key-value /root/.ssh/id_rsa.pub \
   --data-disk-sizes-gb 64
