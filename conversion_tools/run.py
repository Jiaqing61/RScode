# @Time   : 2020/9/18
# @Author : Shanlei Mu
# @Email  : slmu@ruc.edu.cn


import argparse
import importlib

from src.utils import dataset2class, click_dataset, multiple_dataset, multiple_item_features

# Convert raw datasets to atomic datasets
# python RecSysDatasets/conversion_tools/run_ml_resample.py --dataset ml-1m --input_path datasets/raw_data/ml-1m --output_path datasets/ml-1m --convert_inter --convert_item --convert_user
# python RecSysDatasets/conversion_tools/run_ml_resample.py --dataset lastfm-360k --input_path datasets/raw_data/lastfm-360k --output_path datasets/lastfm-360k --convert_inter --convert_user

"""
--dataset
ml-1m
--input_path
../../datasets/raw_data/ml-1m
--output_path
../../datasets/atomic_datasets/ml-1m
--convert_inter
--convert_item
--convert_user
"""

"""
--dataset
lastfm-360k
--input_path
../../datasets/raw_data/lastfm-360k
--output_path
../../datasets/atomic_datasets/lastfm-360k
--convert_inter
--convert_user
"""
if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', type=str, default='ml-1m')
    parser.add_argument('--input_path', type=str, default=None)
    parser.add_argument('--output_path', type=str, default=None)
    parser.add_argument('--interaction_type', type=str, default=None)
    parser.add_argument('--duplicate_removal', action='store_true')

    parser.add_argument('--item_feature_name', type=str, default='none')

    parser.add_argument('--convert_inter', action='store_true')
    parser.add_argument('--convert_item', action='store_true')
    parser.add_argument('--convert_user', action='store_true')

    args = parser.parse_args()

    assert args.input_path is not None, 'input_path can not be None, please specify the input_path'
    assert args.output_path is not None, 'output_path can not be None, please specify the output_path'

    input_args = [args.input_path, args.output_path]
    dataset_class_name = dataset2class[args.dataset.lower()]
    dataset_class = getattr(importlib.import_module('src.extended_dataset'), dataset_class_name)
    if dataset_class_name in multiple_dataset:
        input_args.append(args.interaction_type)
    if dataset_class_name in click_dataset:
        input_args.append(args.duplicate_removal)
    if dataset_class_name in multiple_item_features:
        input_args.append(args.item_feature_name)
    datasets = dataset_class(*input_args)

    if args.convert_inter:
        datasets.convert_inter()
    if args.convert_item:
        datasets.convert_item()
    if args.convert_user:
        datasets.convert_user()
