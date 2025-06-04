#!/bin/bash

cd ${PWD}
git add . 
git commit -m "backup-`date`"
git push origin
