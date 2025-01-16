#################
VPP-GERRIT-REPORT
#################

VPP Gerrit Report categorizes the state of the gerrit.fd.io review queue.  Each gerrit change is labeled with the following status:

========================== ===========================
Status Complete            Needs To Be Addressed
========================== ===========================
V - verified               v - not verified
E - not expired            e - expired
C - no unresolved comments c - comments not resolved
R - reviewed/approved      r - review incomplete
A - abandoned              A - gerrit.fd.io to restore
# - days since update      # - days since update > 30
========================== ===========================

Example: [VECr 23]
    - Verified
    - Not Expired
    - No unresolved comments
    - Review incomplete (Code-Review < +1)
    - 23 days since last update

The report generator sorts the gerrit changes into three categories based on the state and the person or group required to perform the next action:

- Committers:
  Status [VECR xx]: Gerrit Changes that have been verified, are not expired, no unresolved comments, & approved by a maintainer.
  Action: A committer should do a final review and submit the change or provide comment(s).

- Maintainers:
  Status [VECr]: Gerrit Changes that have been verified, are not expired, no unresolved comments, & not reviewed
  Action: The Maintainer should do a code review

- Authors:
  Status <other>: Gerrit Changes that are either not verified, expired, or comments not resolved
  Action: Author should rebase the change, fix verification errors, and/or resolve comments to move the status to [VECr]# Gerrit open patches processing tool

Here is the latest VPP Gerrit Report:
-------------------------------------

==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Thursday 2025-01-16, 02:18:51
--------------------------------------------


Legend:
-------
========================== ===========================
Status Complete            Needs To Be Addressed
========================== ===========================
V - verified               v - not verified
E - not expired            e - expired
C - no unresolved comments c - comments not resolved
R - reviewed/approved      r - review incomplete
A - abandoned              A - gerrit.fd.io to restore
# - days since update      # - days since update > 30
========================== ===========================

Example: [VECr 23]
    - Verified
    - Not Expired
    - Comments resolved
    - Review incomplete (Code-Review < +1)
    - 23 days since last update


Maintainers:
------------
| **Please review these gerrit changes.**

| **NOTE: Gerrit changes may be included under more than one feature based on the modified files regardless of the feature list included on the commit headline.**

af_packet: **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>
  | `42083 <https:////gerrit.fd.io/r/c/vpp/+/42083>`_ [VECr 9]: af_packet: worker thread call vlib_log coredump
  | `41994 <https:////gerrit.fd.io/r/c/vpp/+/41994>`_ [VECr 29]: af_packet: fix crash on af_packet_fd_error

arp: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `42082 <https:////gerrit.fd.io/r/c/vpp/+/42082>`_ [VECr 0]: arp: fix command resolve and config filed exist differ

build: **Damjan Marion** <damarion@cisco.com>
  | `42141 <https:////gerrit.fd.io/r/c/vpp/+/42141>`_ [VECr 0]: af_xdp: fix af_xdp compile waring for clang compiler
  | `42113 <https:////gerrit.fd.io/r/c/vpp/+/42113>`_ [VECr 6]: build: support anolis8 operation for vpp
  | `41259 <https:////gerrit.fd.io/r/c/vpp/+/41259>`_ [VECr 9]: vppinfra: add ARM neoverse-v2 support

classify: **Dave Barach** <vpp@barachs.net>
  | `42034 <https:////gerrit.fd.io/r/c/vpp/+/42034>`_ [VECr 29]: classify: cli filter support for dynamic delete

cnat: **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Neale Ranns** <neale@graphiant.com>
  | `42066 <https:////gerrit.fd.io/r/c/vpp/+/42066>`_ [VECr 23]: cnat: fix udp checksum calculation

crypto: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>
  | `42116 <https:////gerrit.fd.io/r/c/vpp/+/42116>`_ [VECr 1]: vnet: add async algo support for ctr sha2

dev: **Damjan Marion** <damarion@cisco.com>
  | `42110 <https:////gerrit.fd.io/r/c/vpp/+/42110>`_ [VECr 6]: dev: add cli show dev class

dns: **Dave Barach** <vpp@barachs.net>
  | `42074 <https:////gerrit.fd.io/r/c/vpp/+/42074>`_ [VECr 4]: dns: dns api, cli and vat resolve interface implements
  | `42072 <https:////gerrit.fd.io/r/c/vpp/+/42072>`_ [VECr 9]: dns: dns resolution optimisation and bug fixes
  | `42041 <https:////gerrit.fd.io/r/c/vpp/+/42041>`_ [VECr 28]: dns: did't shall resolve before enable

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `40890 <https:////gerrit.fd.io/r/c/vpp/+/40890>`_ [VECr 8]: vlib: fix seed parse error
  | `42059 <https:////gerrit.fd.io/r/c/vpp/+/42059>`_ [VECr 25]: tests: fix docs compile syntax warning

hs-test: **Florin Coras** <fcoras@cisco.com>, **Matus Fabian** <matfabia@cisco.com>, **Adrian Villin** <avillin@cisco.com>
  | `42137 <https:////gerrit.fd.io/r/c/vpp/+/42137>`_ [VECr 2]: http: target parsing improvement

hsa: **Florin Coras** <fcoras@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>
  | `42137 <https:////gerrit.fd.io/r/c/vpp/+/42137>`_ [VECr 2]: http: target parsing improvement

http: **Florin Coras** <fcoras@cisco.com>
  | `42137 <https:////gerrit.fd.io/r/c/vpp/+/42137>`_ [VECr 2]: http: target parsing improvement

http_static: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `42137 <https:////gerrit.fd.io/r/c/vpp/+/42137>`_ [VECr 2]: http: target parsing improvement

ip-neighbor: **Neale Ranns** <neale@graphiant.com>
  | `42150 <https:////gerrit.fd.io/r/c/vpp/+/42150>`_ [VECr 0]: tests: reduce sleep interval in ip-neighbor age test

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `42123 <https:////gerrit.fd.io/r/c/vpp/+/42123>`_ [VECr 6]: ip: skip options handling for locally originated packets

l2: **John Lo** <lojultra2020@outlook.com>, **Steven Luong** <sluong@cisco.com>
  | `42112 <https:////gerrit.fd.io/r/c/vpp/+/42112>`_ [VECr 0]: l2: fix segment fault

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `42123 <https:////gerrit.fd.io/r/c/vpp/+/42123>`_ [VECr 6]: ip: skip options handling for locally originated packets
  | `39518 <https:////gerrit.fd.io/r/c/vpp/+/39518>`_ [VECr 6]: linux-cp: Add VRF synchronization
  | `42065 <https:////gerrit.fd.io/r/c/vpp/+/42065>`_ [VECr 6]: linux-cp: fix segfault while receiving nl messages

octeon: **Monendra Singh Kushwaha** <kmonendra@marvell.com>, **Damjan Marion** <damarion@cisco.com>
  | `42144 <https:////gerrit.fd.io/r/c/vpp/+/42144>`_ [VECr 1]: octeon: add async algo support for ctr sha2
  | `42098 <https:////gerrit.fd.io/r/c/vpp/+/42098>`_ [VECr 1]: octeon: rework octeon crypto framework

session: **Florin Coras** <fcoras@cisco.com>
  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VECr 25]: session: make local port allocator fib aware

snort: **Damjan Marion** <damarion@cisco.com>
  | `41970 <https:////gerrit.fd.io/r/c/vpp/+/41970>`_ [VECr 1]: snort: support multiple instances per interface

sr: **Pablo Camarillo** <pcamaril@cisco.com>, **Ahmed Abdelsalam** <ahabdels@cisco.com>
  | `41533 <https:////gerrit.fd.io/r/c/vpp/+/41533>`_ [VECr 6]: sr: fix sr_policy fib table

svm: **Dave Barach** <vpp@barachs.net>
  | `42050 <https:////gerrit.fd.io/r/c/vpp/+/42050>`_ [VECr 6]: svm: improve ooo try collect

tcp: **Florin Coras** <fcoras@cisco.com>
  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VECr 25]: session: make local port allocator fib aware

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `42150 <https:////gerrit.fd.io/r/c/vpp/+/42150>`_ [VECr 0]: tests: reduce sleep interval in ip-neighbor age test
  | `41970 <https:////gerrit.fd.io/r/c/vpp/+/41970>`_ [VECr 1]: snort: support multiple instances per interface
  | `42044 <https:////gerrit.fd.io/r/c/vpp/+/42044>`_ [VECr 28]: build: fix coverage for various lcov versions

udp: **Florin Coras** <fcoras@cisco.com>
  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VECr 25]: session: make local port allocator fib aware

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `40890 <https:////gerrit.fd.io/r/c/vpp/+/40890>`_ [VECr 8]: vlib: fix seed parse error

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `41259 <https:////gerrit.fd.io/r/c/vpp/+/41259>`_ [VECr 9]: vppinfra: add ARM neoverse-v2 support

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Akeel Ali** <akeelapi@gmail.com>:

  | `42124 <https:////gerrit.fd.io/r/c/vpp/+/42124>`_ [VEc 0]: linux-cp: Add support for LACP packets

**Alexander Slesarev** <aslesare@cisco.com>:

  | `41722 <https:////gerrit.fd.io/r/c/vpp/+/41722>`_ [VeC 37]: libmemif: Fixed strlcpy symbol detection.

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `41210 <https:////gerrit.fd.io/r/c/vpp/+/41210>`_ [vEC 0]: build: disable the "new" way of handling API dependencies which relies on a broken CMake feature
  | `41914 <https:////gerrit.fd.io/r/c/vpp/+/41914>`_ [vEc 5]: pvti: add a doc with write-up, and fix CLI help
  | `41203 <https:////gerrit.fd.io/r/c/vpp/+/41203>`_ [VeC 97]: acl: use ip4_preflen_to_mask instead of artisanal function
  | `41427 <https:////gerrit.fd.io/r/c/vpp/+/41427>`_ [veC 114]: TEST: remove a DVR test on 22.04

**Bence Romsics** <bence.romsics@gmail.com>:

  | `41277 <https:////gerrit.fd.io/r/c/vpp/+/41277>`_ [VeC 140]: vat2: fix -p in vat2 help text
  | `40402 <https:////gerrit.fd.io/r/c/vpp/+/40402>`_ [VeC 142]: docs: Restore and update nat section of progressive tutorial
  | `41399 <https:////gerrit.fd.io/r/c/vpp/+/41399>`_ [VeC 156]: docs: vpp_papi example script

**Damjan Marion** <dmarion@0xa5.net>:

  | `42151 <https:////gerrit.fd.io/r/c/vpp/+/42151>`_ [vEC 0]: crypto: combine sdync and async algs and ops

**Dau Do** <daudo@yahoo.com>:

  | `41966 <https:////gerrit.fd.io/r/c/vpp/+/41966>`_ [VEc 1]: classify: add options to filter out the geneve packets
  | `41538 <https:////gerrit.fd.io/r/c/vpp/+/41538>`_ [veC 100]: memif: add support for per queue counters

**Dave Wallace** <dwallacelf@gmail.com>:

  | `40537 <https:////gerrit.fd.io/r/c/vpp/+/40537>`_ [vEC 6]: misc: patch to test CI infra changes

**Dmitry Valter** <dvalter@protonmail.com>:

  | `40697 <https:////gerrit.fd.io/r/c/vpp/+/40697>`_ [VeC 96]: fib: fix mpls tunnel restacking
  | `40478 <https:////gerrit.fd.io/r/c/vpp/+/40478>`_ [VeC 96]: vlib: add config for elog tracing
  | `40122 <https:////gerrit.fd.io/r/c/vpp/+/40122>`_ [VeC 133]: vppapigen: fix enum format function

**Filip Tehlar** <filip.tehlar@gmail.com>:

  | `41467 <https:////gerrit.fd.io/r/c/vpp/+/41467>`_ [VeC 146]: qos: fix qos record cli

**Florian Larysch** <fl@n621.de>:

  | `41961 <https:////gerrit.fd.io/r/c/vpp/+/41961>`_ [VeC 40]: build: fix PATH with multiple /usr/lib* matches

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `41099 <https:////gerrit.fd.io/r/c/vpp/+/41099>`_ [VeC 33]: vlib: require main core with 'skip-cores' attribute
  | `41985 <https:////gerrit.fd.io/r/c/vpp/+/41985>`_ [VeC 36]: api: fix crash in pcap capture api

**Kai Ji** <kai.ji@intel.com>:

  | `42042 <https:////gerrit.fd.io/r/c/vpp/+/42042>`_ [VEc 27]: dpdk: add in the VLAN offload flag for the iavf PMD driver

**Klement Sekera** <klement.sekera@gmail.com>:

  | `41935 <https:////gerrit.fd.io/r/c/vpp/+/41935>`_ [VeC 50]: ip: fix ICMP inner payload parsing

**Kyle McClammy** <kylem@serverforge.org>:

  | `41705 <https:////gerrit.fd.io/r/c/vpp/+/41705>`_ [veC 94]: Enabled building net_sfc driver in dpdk.mk Added SFN7042Q adapter and virtual functions to init.c and driver.c

**Lajos Katona** <katonalala@gmail.com>:

  | `40898 <https:////gerrit.fd.io/r/c/vpp/+/40898>`_ [Vec 49]: vxlan: move vxlan-gpe to a plugin
  | `40460 <https:////gerrit.fd.io/r/c/vpp/+/40460>`_ [Vec 49]: api: Refresh VPP API language with path background
  | `40471 <https:////gerrit.fd.io/r/c/vpp/+/40471>`_ [Vec 49]: docs: Add doc for API Trace Tools
  | `41545 <https:////gerrit.fd.io/r/c/vpp/+/41545>`_ [vec 126]: api-trace: enable both rx and tx direction

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `41435 <https:////gerrit.fd.io/r/c/vpp/+/41435>`_ [VeC 110]: vppinfra: add ARM Neoverse-V1 support

**Monendra Singh Kushwaha** <kmonendra@marvell.com>:

  | `41698 <https:////gerrit.fd.io/r/c/vpp/+/41698>`_ [VeC 98]: octeon: register callback to set max npa pools
  | `41459 <https:////gerrit.fd.io/r/c/vpp/+/41459>`_ [Vec 112]: dev: add support for vf device with vf_token
  | `41458 <https:////gerrit.fd.io/r/c/vpp/+/41458>`_ [Vec 114]: vlib: add vfio-token parsing support

**Nikita Skrynnik** <nikita.skrynnik@xored.com>:

  | `40246 <https:////gerrit.fd.io/r/c/vpp/+/40246>`_ [VEc 22]: ping: Check only PING_RESPONSE_IP4 and PING_RESPONSE_IP6 events
  | `40325 <https:////gerrit.fd.io/r/c/vpp/+/40325>`_ [VEc 22]: ping: Allow to specify a source interface in ping binary API

**Ole Troan** <otroan@employees.org>:

  | `41342 <https:////gerrit.fd.io/r/c/vpp/+/41342>`_ [Vec 90]: ip6: don't forward packets with invalid source address

**Pierre Pfister** <ppfister@cisco.com>:

  | `42032 <https:////gerrit.fd.io/r/c/vpp/+/42032>`_ [vEC 29]: clib: add full simulated time support

**Pim van Pelt** <pim@ipng.nl>:

  | `41680 <https:////gerrit.fd.io/r/c/vpp/+/41680>`_ [VeC 35]: sflow: initial checkin

**Rabei Becheikh** <rabei.becheikh@enigmedia.es>:

  | `41519 <https:////gerrit.fd.io/r/c/vpp/+/41519>`_ [VeC 135]: flowprobe: Fix the problem of Network Byte Order for Ethernet type
  | `41518 <https:////gerrit.fd.io/r/c/vpp/+/41518>`_ [veC 135]: flowprobe:   Fix the problem of Network Byte Order for Ethernet type Type: fix
  | `41517 <https:////gerrit.fd.io/r/c/vpp/+/41517>`_ [veC 135]: flowprobe: Fix the problem of  Network Byte Order for Ethernet type Type: fix
  | `41516 <https:////gerrit.fd.io/r/c/vpp/+/41516>`_ [veC 135]: flowprobe:Fix the problem of  Network Byte Order for Ethernet type Type:fix
  | `41515 <https:////gerrit.fd.io/r/c/vpp/+/41515>`_ [veC 135]: flowprobe:   Fix the problem of  Network Byte Order for Ethernet type Type: fix
  | `41514 <https:////gerrit.fd.io/r/c/vpp/+/41514>`_ [veC 135]: fowprobe:   Fix the problem with Network Byte Order for Ethernet type Type: fix
  | `41513 <https:////gerrit.fd.io/r/c/vpp/+/41513>`_ [veC 135]: Flowprobe: Fix etherType value for IPFIX (Network Byte Order) Type: Fix
  | `41512 <https:////gerrit.fd.io/r/c/vpp/+/41512>`_ [veC 135]: Flowprobe: Fix etherType Type:Fix
  | `41509 <https:////gerrit.fd.io/r/c/vpp/+/41509>`_ [veC 135]: flowprobe: Fix the problem with Network Byte Order for Ethernet type field and modify test
  | `41510 <https:////gerrit.fd.io/r/c/vpp/+/41510>`_ [veC 135]: flowprobe:   Fix the problem with Network Byte Order for Ethernet type and modify the test Type: fix
  | `41507 <https:////gerrit.fd.io/r/c/vpp/+/41507>`_ [veC 135]: flowprobe: Fix the problem with Network Byte Order for Ethernet type field
  | `41506 <https:////gerrit.fd.io/r/c/vpp/+/41506>`_ [veC 135]: docs: Fix the problem with Network Byte Order for Ethernet type field Type:fix
  | `41505 <https:////gerrit.fd.io/r/c/vpp/+/41505>`_ [veC 135]: docs: Fix the problem with Network Byte Order for Ethernet type field Type: fix

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `41678 <https:////gerrit.fd.io/r/c/vpp/+/41678>`_ [VeC 93]: linux-cp: do ip6-ll cleanup on interface removal

**Varun Rapelly** <vrapelly@marvell.com>:

  | `42070 <https:////gerrit.fd.io/r/c/vpp/+/42070>`_ [VEc 0]: tls:async event handling enhancement
  | `42119 <https:////gerrit.fd.io/r/c/vpp/+/42119>`_ [VEc 5]: tls: added dpdk engine support

**Vinod Krishna** <vinod.krishna@arm.com>:

  | `41979 <https:////gerrit.fd.io/r/c/vpp/+/41979>`_ [vEC 8]: build: support 128B/64B cache-line size in Arm image

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `40626 <https:////gerrit.fd.io/r/c/vpp/+/40626>`_ [Vec 142]: ip6-nd: simplify API to directly set options

**Vladimir Smirnov** <civil.over@gmail.com>:

  | `42121 <https:////gerrit.fd.io/r/c/vpp/+/42121>`_ [VEc 0]: dpdk: bump to DPDK 24.11.1
  | `42126 <https:////gerrit.fd.io/r/c/vpp/+/42126>`_ [VEc 0]: dpdk: update rdma-core to 55.0
  | `42086 <https:////gerrit.fd.io/r/c/vpp/+/42086>`_ [VEc 1]: build: add support for debian trixie
  | `42090 <https:////gerrit.fd.io/r/c/vpp/+/42090>`_ [VEc 7]: build: Add VLIB_MAX_NELTS configure option
  | `42089 <https:////gerrit.fd.io/r/c/vpp/+/42089>`_ [vEc 7]: fix: fail in runtime if workers > nelts

**Vladislav Grishenko** <themiron@mail.ru>:

  | `40628 <https:////gerrit.fd.io/r/c/vpp/+/40628>`_ [VeC 41]: stats: add sw interface tags to statseg
  | `40627 <https:////gerrit.fd.io/r/c/vpp/+/40627>`_ [VeC 49]: fib: fix invalid udp encap id cases
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VeC 49]: fib: fix udp encap mp-safe ops and id validation
  | `40630 <https:////gerrit.fd.io/r/c/vpp/+/40630>`_ [VeC 52]: vlib: mark cli quit command as mp_safe
  | `41657 <https:////gerrit.fd.io/r/c/vpp/+/41657>`_ [VeC 96]: nat: make nat44-ed cli summary less verbose
  | `37263 <https:////gerrit.fd.io/r/c/vpp/+/37263>`_ [VeC 100]: nat: add nat44-ed session filtering by fib table
  | `41660 <https:////gerrit.fd.io/r/c/vpp/+/41660>`_ [VeC 107]: nat: add nat44-ed ipfix dst address and port logging
  | `41659 <https:////gerrit.fd.io/r/c/vpp/+/41659>`_ [VeC 107]: nat: make nat44-ed api dumps & cli show mp-safe
  | `41658 <https:////gerrit.fd.io/r/c/vpp/+/41658>`_ [VeC 107]: nat: fix nat44-ed per-vrf session limit and tests
  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [VeC 107]: mpls: fix crashes on mpls tunnel create/delete
  | `41656 <https:////gerrit.fd.io/r/c/vpp/+/41656>`_ [VeC 107]: nat: pass nat44-ed packets with ttl=1 on outside interfaces
  | `41615 <https:////gerrit.fd.io/r/c/vpp/+/41615>`_ [VeC 107]: mpls: clang-format mpls-tunnel for upcoming changes
  | `40413 <https:////gerrit.fd.io/r/c/vpp/+/40413>`_ [VeC 107]: nat: stick nat44-ed to use configured outside-fib
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VeC 107]: nat: fix nat44-ed address removal from fib
  | `38524 <https:////gerrit.fd.io/r/c/vpp/+/38524>`_ [VeC 107]: fib: fix interface resolve from unlinked fib entries
  | `39579 <https:////gerrit.fd.io/r/c/vpp/+/39579>`_ [VeC 107]: fib: ensure mpls dpo index is valid for its next node
  | `40629 <https:////gerrit.fd.io/r/c/vpp/+/40629>`_ [VeC 107]: stats: add interface link speed to statseg

**Vratko Polak** <vrpolak@cisco.com>:

  | `41558 <https:////gerrit.fd.io/r/c/vpp/+/41558>`_ [VeC 107]: avf: mark api as deprecated
  | `41557 <https:////gerrit.fd.io/r/c/vpp/+/41557>`_ [VeC 113]: dev: declare api as production
  | `41552 <https:////gerrit.fd.io/r/c/vpp/+/41552>`_ [VeC 127]: avf: interprocess reply via pointer

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `41594 <https:////gerrit.fd.io/r/c/vpp/+/41594>`_ [Vec 111]: http: fix timer pool assert crash due to timer freed when timeout in main thread

**lei feng** <1579628578@qq.com>:

  | `42129 <https:////gerrit.fd.io/r/c/vpp/+/42129>`_ [VEc 1]: dns: support ipv6 server to resolve name
  | `42064 <https:////gerrit.fd.io/r/c/vpp/+/42064>`_ [VEc 6]: docs: Python apis examples
  | `42056 <https:////gerrit.fd.io/r/c/vpp/+/42056>`_ [vEC 25]: docs: Python apis examples
  | `42055 <https:////gerrit.fd.io/r/c/vpp/+/42055>`_ [vEC 25]: docs: Python apis examples
  | `41866 <https:////gerrit.fd.io/r/c/vpp/+/41866>`_ [VEc 28]: dns: did't shall resolve before enable
  | `42040 <https:////gerrit.fd.io/r/c/vpp/+/42040>`_ [vEC 28]: docs: add examples for VXLAN tunnel
  | `42039 <https:////gerrit.fd.io/r/c/vpp/+/42039>`_ [vEC 28]: docs: add examples for GRE teb tunnel
  | `41863 <https:////gerrit.fd.io/r/c/vpp/+/41863>`_ [VeC 55]: build: ubuntu24.04 llvm[18] lack of the header and library of asan
  | `41860 <https:////gerrit.fd.io/r/c/vpp/+/41860>`_ [veC 55]: build: ubuntu24.04 llvm[18] lack of the header and library of asan
  | `41855 <https:////gerrit.fd.io/r/c/vpp/+/41855>`_ [VeC 56]: svm: fix check bitmap logic error
  | `41854 <https:////gerrit.fd.io/r/c/vpp/+/41854>`_ [veC 56]: svm: fix check bitmap logic error
  | `41852 <https:////gerrit.fd.io/r/c/vpp/+/41852>`_ [veC 56]: svm: fix check bitmap logic error
  | `41851 <https:////gerrit.fd.io/r/c/vpp/+/41851>`_ [veC 56]: svm: fix check bitmap logic error
  | `41850 <https:////gerrit.fd.io/r/c/vpp/+/41850>`_ [veC 56]: Makefile: support anolis8 operation for vpp
  | `41848 <https:////gerrit.fd.io/r/c/vpp/+/41848>`_ [veC 56]: Makefile: support anolis8 operation for vpp Type: improvement

**shaohui jin** <jinshaohui789@163.com>:

  | `41652 <https:////gerrit.fd.io/r/c/vpp/+/41652>`_ [veC 55]: dhcp:fix dhcp server no support Option 82,unable to assign an IP address.
  | `41653 <https:////gerrit.fd.io/r/c/vpp/+/41653>`_ [veC 55]: dhcp:dhcp request packets always use the first server address.

**sonsumin** <itoodo12@gmail.com>:

  | `41681 <https:////gerrit.fd.io/r/c/vpp/+/41681>`_ [VeC 80]: nat: refactor argument order for nat44-ed static mapping
  | `41667 <https:////gerrit.fd.io/r/c/vpp/+/41667>`_ [veC 105]: refactor(nat44): change argument order and parsing format for static mapping

Legend:
-------
========================== ===========================
Status Complete            Needs To Be Addressed
========================== ===========================
V - verified               v - not verified
E - not expired            e - expired
C - no unresolved comments c - comments not resolved
R - reviewed/approved      r - review incomplete
A - abandoned              A - gerrit.fd.io to restore
# - days since update      # - days since update > 30
========================== ===========================

Example: [VECr 23]
    - Verified
    - Not Expired
    - Comments resolved
    - Review incomplete (Code-Review < +1)
    - 23 days since last update


Statistics:
-----------
================ ===
Patches assigned
================ ===
authors          99
maintainers      28
committers       0
abandoned        0
================ ===

