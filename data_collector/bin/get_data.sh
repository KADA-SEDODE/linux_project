#!/bin/bash
source ../conf/collector.conf

echo "Form ID is set as: ${form_id}"
echo "Target path is set as: ${target_path}"

python collect_data.py
