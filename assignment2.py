#! /usr/bin/env python3

import vcf

__author__ = 'Tamás Gutsohn'

vcffile = 'AmpliseqExome.20141120.NA24385.vcf'

class Assignment2:
    def __init__(self):
        ## Check if pyvcf is installed
        print("PyVCF version: %s" % vcf.VERSION)

    def get_average_quality_of_son(self):
        vcf_reader = vcf.Reader(open(vcffile, 'r'))
        numbers = []
        for record in vcf_reader:
            numbers.append(record.QUAL)
        avgquality = float(sum(numbers)/ max(len(numbers), 1))
        print('Average Quality of son: ', avgquality)

    def get_total_number_of_variants_of_son(self):
        vcf_reader = vcf.Reader(open(vcffile, 'r'))
        numbers = []
        for record in vcf_reader:
            numbers.append(record.QUAL)
        print('\nTotal number of variants of son: ', len(numbers))

    def get_variant_caller_of_vcf(self):
        vcf_reader = vcf.Reader(open(vcffile, 'r'))
        print('\nVariant caller of vcf: ', vcf_reader.metadata['source'])

    def get_human_reference_version(self):
        vcf_reader = vcf.Reader(open(vcffile, 'r'))
        print('\nHuman reference version: ', vcf_reader.metadata['reference'])

    def get_number_of_indels(self):
        vcf_reader = vcf.Reader(open(vcffile, 'r'))
        indels = 0
        for record in vcf_reader:
            if record.is_indel == True:
                indels += 1
        print('\nNumber of indels: ', indels)

    def get_number_of_snvs(self):
        vcf_reader = vcf.Reader(open(vcffile, 'r'))
        snvs = 0
        for record in vcf_reader:
            if record.is_snp == True:
                snvs += 1
        print('\nNumber of snvs: ', snvs)
    def get_number_of_heterozygous_variants(self):
        vcf_reader = vcf.Reader(open(vcffile, 'r'))
        hetvar = 0
        for record in vcf_reader:
            if record.num_het > 0:
                hetvar += 1
        print('\nNumber of heterozygous variants: ', hetvar)

    def print_summary(self):
        print("Print all results here:\n")


if __name__ == '__main__':
    print("Assignment 2")
    assignment1 = Assignment2()
    assignment1.print_summary()
    assignment1.get_average_quality_of_son()
    assignment1.get_total_number_of_variants_of_son()
    assignment1.get_variant_caller_of_vcf()
    assignment1.get_human_reference_version()
    assignment1.get_number_of_indels()
    assignment1.get_number_of_snvs()
    assignment1.get_number_of_heterozygous_variants()