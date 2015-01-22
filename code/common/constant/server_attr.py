# coding=utf-8
'''
tag中定义常量
'''

# 下面是服务器module的form参数(select).
# TODO 格式为：(value, 显示值, 是否为默认值),1表示为默认值

DEVICE_CLASS_CHOICES = [
    ('A1', 'A1'),
    ('A3', 'A3'),
    ('A5', 'A5'),
    ('A1-HP', 'A1-HP'),
    ('B1', 'B1'),
    ('B2', 'B2'),
    ('B4', 'B4'),
    ('B5', 'B5'),
    ('B6', 'B6'),
    ('C1', 'C1'),
    ('RC1', 'RC1'),
    ('VC2', 'VC2'),
    ('VC3', 'VC3'),
    ('VB2', 'VB2'),
    ('VB3', 'VB3'),
    ('VB4', 'VB4'),
]

LOGIC_ZONE_CHOICES = [
    (u"普通区", u"普通区"),
    (u"X专区",  u"X专区"),
    (u"OSS区",  u"OSS区"),
    (u"DEVNET区",  u"DEVNET区"),
    (u"合作专区",  u"合作专区"),
]

RAID_TYPE_CHOICES = [
    ('No Raid', 'No Raid'),
    ('Raid0', 'Raid0'),
    ('Raid0+1', 'Raid0+1'),
    ('Raid1', 'Raid1'),
    ('Raid1+0', 'Raid1+0'),
    ('6*2Raid1', '6*2Raid1'),
    ('Raid5', 'Raid5'),
    ('Raid6', 'Raid6'),
    ('2Raid1+4Raid5', '2Raid1+4Raid5'),
    ('2raid1+10raid5', '2raid1+10raid5'),
    ('2RAID1+10RAID10', '2RAID1+10RAID10'),
    ('4RAID5+8RAID10', '4RAID5+8RAID10'),
    ('2 Raid1+6 Raid10', '2 Raid1+6 Raid10'),
    ('2 raid1+10 no raid', '2 raid1+10 no raid'),
    ('2raid1+5raid5+5raid5', '2raid1+5raid5+5raid5'),
#    ('Raid1:2*73G(os),raid10/01:4*300G(data)(优先10)', 'Raid1:2*73G(os),raid10/01:4*300G(data)(优先10)'),
#    ('Raid1:2*146G(os),raid10/01:4*146G(data)(优先10)', 'Raid1:2*146G(os),raid10/01:4*146G(data)(优先10)'),
]

OS_CHOICES = [
    ('SUSE Linux Enterprise Server 10 (i586)', 'SUSE Linux Enterprise Server 10 (i586)'),
    ('SUSE Linux Enterprise Server 10 (x86_64)', 'SUSE Linux Enterprise Server 10 (x86_64)'),
    #('SUSE Linux Enterprise Server 10 for xen (i586)', 'SUSE Linux Enterprise Server 10 for xen (i586)'),# buyao
    ('SUSE Linux Enterprise Server 11 (x86_64)', 'SUSE Linux Enterprise Server 11 (x86_64)'),
    ('SUSE Linux Enterprise Server 11 for xen (x86_64)', 'SUSE Linux Enterprise Server 11 for xen (x86_64)'),
    #('SUSE Linux Enterprise Server 11 SP1 for xen (x86_64)', 'SUSE Linux Enterprise Server 11 SP1 for xen (x86_64)'),# buyao
    ('tlinux-SUSE10 (x86_64)', 'tlinux-SUSE10 (x86_64)'),
    #('Tencent tlinux release 1.0 (Final)', 'Tencent tlinux release 1.0 (Final)'),# buyao
    ('Tencent tlinux release 1.2 (Final)', 'Tencent tlinux release 1.2 (Final)'),
    ('XServer V3.2', 'XServer V3.2'),
    ('XServer V3.2 for OA', 'XServer V3.2 for OA'),
    ('XServer V3.2_64', 'XServer V3.2_64'),
    ('XServer V8.1_64', 'XServer V8.1_64'),
]

