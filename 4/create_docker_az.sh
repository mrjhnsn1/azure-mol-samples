#!/bin/bash
docker run -it  -v ${HOME}/devl/az_scripts:/az_scripts -v ${HOME}/.ssh:/root/.ssh:ro mcr.microsoft.com/azure-cli
