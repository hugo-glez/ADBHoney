cmd_responses = {}
cmd_responses['ls'] = "acct\n\
bt_firmware\n\
bugreports\n\
cache\ncharger\nconfig\nd\ndata\ndev\ndsp\netc\nfirmware\nmnt\nnonplat_file_contexts\nnonplat_property_contexts\nnonplat_seapp_contexts\noem\npersist\nplat_file_contexts\nplat_property_contexts\nplat_seapp_contexts\nplat_service_contexts\nproc\nres\nroot\nsbin\nsdcard\nsepolicy\nstorage\nsys\nsystem\ntombstones\nvendor\nls: ./vndservice_contexts: Permission denied\nls: ./ueventd.rc: Permission denied\nls: ./plat_hwservice_contexts: Permission denied\nls: ./nonplat_service_contexts: Permission denied\nls: ./nonplat_hwservice_contexts: Permission denied\nls: ./init.zygote64_32.rc: Permission denied\nls: ./init.zygote32.rc: Permission denied\nls: ./init.usb.rc: Permission denied\nls: ./init.usb.configfs.rc: Permission denied\nls: ./init.rc: Permission denied\nls: ./init.environ.rc: Permission denied\nls: ./init: Permission denied\nls: ./default.prop: Permission denied\n"

cmd_responses['ps'] = "\
USER      PID   PPID  VSIZE  RSS   WCHAN              PC NAME \n\
root      1     0     19348  888            0 0000000000 S /init \n\
root      2     0     0      0              0 0000000000 S kthreadd\n\
root      3     2     0      0              0 0000000000 S ksoftirqd/0\n\
root      5     2     0      0              0 0000000000 S kworker/0:0H\n\
root      7     2     0      0              0 0000000000 S rcu_preempt\n\
root      8     2     0      0              0 0000000000 S rcu_sched\n\
root      9     2     0      0              0 0000000000 S rcu_bh\n\
root      10    2     0      0              0 0000000000 S migration/0\n\
root      11    2     0      0              0 0000000000 S watchdog/0\n\
root      12    2     0      0              0 0000000000 S watchdog/1\n\
root      13    2     0      0              0 0000000000 S migration/1\n\
root      14    2     0      0              0 0000000000 S ksoftirqd/1\n\
root      16    2     0      0              0 0000000000 S kworker/1:0H\n\
root      17    2     0      0              0 0000000000 S watchdog/2\n\
root      18    2     0      0              0 0000000000 S migration/2\n\
root      19    2     0      0              0 0000000000 S ksoftirqd/2\n\
root      21    2     0      0              0 0000000000 S kworker/2:0H\n\
root      22    2     0      0              0 0000000000 S watchdog/3\n\
root      23    2     0      0              0 0000000000 S migration/3\n\
root      24    2     0      0              0 0000000000 S ksoftirqd/3\n\
root      26    2     0      0              0 0000000000 S kworker/3:0H\n\
root      27    2     0      0              0 0000000000 S watchdog/4\n\
root      28    2     0      0              0 0000000000 S migration/4\n\
root      29    2     0      0              0 0000000000 S ksoftirqd/4\n\
root      31    2     0      0              0 0000000000 S kworker/4:0H\n\
root      32    2     0      0              0 0000000000 S watchdog/5\n\
root      33    2     0      0              0 0000000000 S migration/5\n\
root      34    2     0      0              0 0000000000 S ksoftirqd/5\n\
root      36    2     0      0              0 0000000000 S kworker/5:0H\n\
root      37    2     0      0              0 0000000000 S watchdog/6\n\
root      38    2     0      0              0 0000000000 S migration/6\n\
root      39    2     0      0              0 0000000000 S ksoftirqd/6\n\
root      41    2     0      0              0 0000000000 S kworker/6:0H\n\
root      42    2     0      0              0 0000000000 S watchdog/7\n\
root      43    2     0      0              0 0000000000 S migration/7\n\
root      44    2     0      0              0 0000000000 S ksoftirqd/7\n\
root      46    2     0      0              0 0000000000 S kworker/7:0H\n\
root      47    2     0      0              0 0000000000 S khelper\n\
root      48    2     0      0              0 0000000000 S kdevtmpfs\n\
root      49    2     0      0              0 0000000000 S perf\n\
root      50    2     0      0              0 0000000000 D bbox_main\n\
root      53    2     0      0              0 0000000000 S softtimer_nowak\n\
root      54    2     0      0              0 0000000000 S icc_shared\n\
root      55    2     0      0              0 0000000000 S mailbox-10\n\
root      56    2     0      0              0 0000000000 S mailbox-11\n\
root      57    2     0      0              0 0000000000 S mailbox-12\n\
root      58    2     0      0              0 0000000000 S mailbox-13\n\
root      59    2     0      0              0 0000000000 S mailbox-14\n\
root      60    2     0      0              0 0000000000 S mailbox-15\n\
root      61    2     0      0              0 0000000000 S mailbox-16\n\
root      62    2     0      0              0 0000000000 S mailbox-17\n\
root      63    2     0      0              0 0000000000 S mailbox-18\n\
root      64    2     0      0              0 0000000000 S mailbox-25\n\
root      65    2     0      0              0 0000000000 S mailbox-26\n\
root      66    2     0      0              0 0000000000 S mailbox-27\n\
root      67    2     0      0              0 0000000000 S mailbox-28\n\
root      68    2     0      0              0 0000000000 S mailbox-29\n\
root      69    2     0    \n" 


other_responses = {} 
other_responses['root'] = "adbd cannot run as root in production builds"

