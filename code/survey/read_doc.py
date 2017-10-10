#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
# import textract

from docx import opendocx, getdocumenttext

from mysql import query, query_one, save

def get_file_path():
    all_path = os.walk('/mnt/hgfs/Data/work/满意度调查/')

    doc_files = []
    docx_files = []
    for path in all_path:
        for file in path[-1]:
            if file.find(".docx") != -1:
                file = "%s/%s" % (path[0], file,)
                docx_files.append(file)
            elif file.find(".doc") != -1:
                file = "%s/%s" % (path[0], file,)
                doc_files.append(file)

    return (doc_files, docx_files,)


def get_enterprise_name(filepath):
    try:
        document = opendocx(filepath)
    except Exception as e:
        return None
    paratextlist = getdocumenttext(document)
    for p in paratextlist:
        if not p.find(u'申报企业'):
            return p.split(u"：")[1]
        else:
            continue

def insert_data(enterprise_name):
    save(sql=u'INSERT INTO `base_enterprise`(`name`) VALUES(%s)', list1=(enterprise_name, ))


def main():
    # filepath = '/mnt/hgfs/Data/work/满意度调查/工业类319个/仙桃工业类4/仙桃市诚宇汽车电器有限公司表四.doc'
    # print textract.process(filepath)
    docx_list = get_file_path()[1]
    for d in docx_list:
        enterprise_name = get_enterprise_name(d)
        if enterprise_name:
            insert_data(enterprise_name)

if __name__ == '__main__':
    main()