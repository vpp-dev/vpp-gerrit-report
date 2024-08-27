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
generated on Tuesday 2024-08-27, 02:14:54
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


Committers:
-----------
| **These gerrit changes have been**

    - Verified
    - Not expired
    - Comments resolved
    - Approved by Maintainers

| **Please perform a final review & submit.**

  | `41474 <https:////gerrit.fd.io/r/c/vpp/+/41474>`_ [VECR 0]: octeon: use proper refs for roc item spec and mask

Maintainers:
------------
| **Please review these gerrit changes.**

| **NOTE: Gerrit changes may be included under more than one feature based on the modified files regardless of the feature list included on the commit headline.**

avf: **Damjan Marion** <damarion@cisco.com>
  | `41343 <https:////gerrit.fd.io/r/c/vpp/+/41343>`_ [VECr 3]: avf: avoid AVF deadlock

build: **Damjan Marion** <damarion@cisco.com>
  | `41481 <https:////gerrit.fd.io/r/c/vpp/+/41481>`_ [VECr 0]: build: fix gcov failure on ubuntu 24.04
  | `41458 <https:////gerrit.fd.io/r/c/vpp/+/41458>`_ [VECr 5]: vlib: add vfio-token parsing support
  | `41355 <https:////gerrit.fd.io/r/c/vpp/+/41355>`_ [VECr 25]: build: Add FreeBSD install-dep support
  | `40971 <https:////gerrit.fd.io/r/c/vpp/+/40971>`_ [VECr 27]: build: add SHA256 checksums for external downloaded dependencies

crypto-native: **Damjan Marion** <damarion@cisco.com>
  | `41362 <https:////gerrit.fd.io/r/c/vpp/+/41362>`_ [VECr 5]: crypto-native: aes_cbc_encrypt in vppinfra

dhcp: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `41272 <https:////gerrit.fd.io/r/c/vpp/+/41272>`_ [VECr 18]: dhcp: fix buffer length after adding new option

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `41314 <https:////gerrit.fd.io/r/c/vpp/+/41314>`_ [VECr 0]: session: add Source Deny List
  | `40402 <https:////gerrit.fd.io/r/c/vpp/+/40402>`_ [VECr 0]: docs: Restore and update nat section of progressive tutorial
  | `41378 <https:////gerrit.fd.io/r/c/vpp/+/41378>`_ [VECr 19]: vat2: docs

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `41168 <https:////gerrit.fd.io/r/c/vpp/+/41168>`_ [VECr 26]: dpdk: xstats as symlinks

hs-test: **Florin Coras** <fcoras@cisco.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Maros Ondrejicka** <maros.ondrejicka@pantheon.tech>
  | `41480 <https:////gerrit.fd.io/r/c/vpp/+/41480>`_ [VECr 0]: http: http_state_wait_app_reply improvement
  | `41479 <https:////gerrit.fd.io/r/c/vpp/+/41479>`_ [VECr 0]: hs-test: http tests improvement

hsa: **Florin Coras** <fcoras@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>
  | `41480 <https:////gerrit.fd.io/r/c/vpp/+/41480>`_ [VECr 0]: http: http_state_wait_app_reply improvement

http: **Florin Coras** <fcoras@cisco.com>
  | `41480 <https:////gerrit.fd.io/r/c/vpp/+/41480>`_ [VECr 0]: http: http_state_wait_app_reply improvement

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `40720 <https:////gerrit.fd.io/r/c/vpp/+/40720>`_ [VECr 21]: ip: added CLI command to set ip6 reassembly params

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `41314 <https:////gerrit.fd.io/r/c/vpp/+/41314>`_ [VECr 0]: session: add Source Deny List
  | `41399 <https:////gerrit.fd.io/r/c/vpp/+/41399>`_ [VECr 14]: docs: vpp_papi example script

pci: **Damjan Marion** <damarion@cisco.com>
  | `41458 <https:////gerrit.fd.io/r/c/vpp/+/41458>`_ [VECr 5]: vlib: add vfio-token parsing support

qos: **Neale Ranns** <neale@graphiant.com>
  | `41467 <https:////gerrit.fd.io/r/c/vpp/+/41467>`_ [VECr 4]: qos: fix qos record cli

session: **Florin Coras** <fcoras@cisco.com>
  | `41314 <https:////gerrit.fd.io/r/c/vpp/+/41314>`_ [VECr 0]: session: add Source Deny List
  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VECr 2]: session: make local port allocator fib aware

tcp: **Florin Coras** <fcoras@cisco.com>
  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VECr 2]: session: make local port allocator fib aware

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `41314 <https:////gerrit.fd.io/r/c/vpp/+/41314>`_ [VECr 0]: session: add Source Deny List
  | `41457 <https:////gerrit.fd.io/r/c/vpp/+/41457>`_ [VECr 4]: tests: remove use of python 2.7 compatibility module 'six'
  | `41272 <https:////gerrit.fd.io/r/c/vpp/+/41272>`_ [VECr 18]: dhcp: fix buffer length after adding new option
  | `40720 <https:////gerrit.fd.io/r/c/vpp/+/40720>`_ [VECr 21]: ip: added CLI command to set ip6 reassembly params

udp: **Florin Coras** <fcoras@cisco.com>
  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VECr 2]: session: make local port allocator fib aware

unittest: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `41314 <https:////gerrit.fd.io/r/c/vpp/+/41314>`_ [VECr 0]: session: add Source Deny List

vapi: **Ole Troan** <ot@cisco.com>
  | `40861 <https:////gerrit.fd.io/r/c/vpp/+/40861>`_ [VECr 14]: vapi: remove plugin dependency from tests

vat2: **Ole Troan** <ot@cisco.com>
  | `41277 <https:////gerrit.fd.io/r/c/vpp/+/41277>`_ [VECr 21]: vat2: fix -p in vat2 help text

vcl: **Florin Coras** <fcoras@cisco.com>
  | `40537 <https:////gerrit.fd.io/r/c/vpp/+/40537>`_ [VECr 0]: misc: patch to test CI infra changes

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `41343 <https:////gerrit.fd.io/r/c/vpp/+/41343>`_ [VECr 3]: avf: avoid AVF deadlock
  | `41094 <https:////gerrit.fd.io/r/c/vpp/+/41094>`_ [VECr 4]: vlib: improve core pinning
  | `41458 <https:////gerrit.fd.io/r/c/vpp/+/41458>`_ [VECr 5]: vlib: add vfio-token parsing support

vpp: **Dave Barach** <vpp@barachs.net>
  | `41094 <https:////gerrit.fd.io/r/c/vpp/+/41094>`_ [VECr 4]: vlib: improve core pinning

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `41094 <https:////gerrit.fd.io/r/c/vpp/+/41094>`_ [VECr 4]: vlib: improve core pinning
  | `41362 <https:////gerrit.fd.io/r/c/vpp/+/41362>`_ [VECr 5]: crypto-native: aes_cbc_encrypt in vppinfra
  | `41410 <https:////gerrit.fd.io/r/c/vpp/+/41410>`_ [VECr 12]: vppinfra: Use affinity for online cpus on FreeBSD

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Adrian Villin** <avillin@cisco.com>:

  | `41417 <https:////gerrit.fd.io/r/c/vpp/+/41417>`_ [VEc 0]: hs-test: added a redis-benchmark test

**Alexander Chernavin** <achernavin@netgate.com>:

  | `41161 <https:////gerrit.fd.io/r/c/vpp/+/41161>`_ [Vec 61]: bonding: make link state depend on active members

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `41210 <https:////gerrit.fd.io/r/c/vpp/+/41210>`_ [vEC 24]: build: disable the "new" way of handling API dependencies which relies on a broken CMake feature
  | `39994 <https:////gerrit.fd.io/r/c/vpp/+/39994>`_ [vec 32]: pvti: Packet Vector Tunnel Interface
  | `41203 <https:////gerrit.fd.io/r/c/vpp/+/41203>`_ [veC 32]: acl: use ip4_preflen_to_mask instead of artisanal function

**Benoît Ganne** <bganne@cisco.com>:

  | `41246 <https:////gerrit.fd.io/r/c/vpp/+/41246>`_ [VeC 39]: pg: fix offload offsets for ip4/6-input

**Dau Do** <daudo@yahoo.com>:

  | `41138 <https:////gerrit.fd.io/r/c/vpp/+/41138>`_ [VeC 68]: ipsec: add binapi to set/get the SA's seq/replay_window
  | `41107 <https:////gerrit.fd.io/r/c/vpp/+/41107>`_ [Vec 72]: hash: Add cli to enable soft interface hashing based on esp
  | `41103 <https:////gerrit.fd.io/r/c/vpp/+/41103>`_ [VeC 75]: ipsec: Add api to show the number of SAs distributed over the workers
  | `41104 <https:////gerrit.fd.io/r/c/vpp/+/41104>`_ [veC 76]: ipsec: Add option to configure the handoff worker queue size
  | `41100 <https:////gerrit.fd.io/r/c/vpp/+/41100>`_ [veC 77]: ipsec: Add option to configure the handoff worker queue size
  | `40831 <https:////gerrit.fd.io/r/c/vpp/+/40831>`_ [veC 121]: ipsec: added CLI command to show the SA's distributed between workers. Added configuration option to adjust the worker queue size. Both of these are used for performance tune-up. In our setting, it's best to set a bigger queue size to avoid the congestion drop. If not set, it's default to current queue size.

**Denys Haryachyy** <garyachy@gmail.com>:

  | `40850 <https:////gerrit.fd.io/r/c/vpp/+/40850>`_ [VeC 105]: ikev2: multiple ts per profile

**Dmitry Valter** <dvalter@protonmail.com>:

  | `40122 <https:////gerrit.fd.io/r/c/vpp/+/40122>`_ [VeC 74]: vppapigen: fix enum format function
  | `40082 <https:////gerrit.fd.io/r/c/vpp/+/40082>`_ [VeC 126]: ip: mark ipX_header_t and ip4_address_t as packed
  | `40697 <https:////gerrit.fd.io/r/c/vpp/+/40697>`_ [VeC 137]: fib: fix mpls tunnel restacking
  | `40478 <https:////gerrit.fd.io/r/c/vpp/+/40478>`_ [VeC 154]: vlib: add config for elog tracing

**Florin Coras** <florin.coras@gmail.com>:

  | `41257 <https:////gerrit.fd.io/r/c/vpp/+/41257>`_ [VeC 45]: api: support api clients with real-time scheduling

**Hadi Dernaika** <hadidernaika31@gmail.com>:

  | `39995 <https:////gerrit.fd.io/r/c/vpp/+/39995>`_ [Vec 166]: virtio: fix crash on show tun cli

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `41099 <https:////gerrit.fd.io/r/c/vpp/+/41099>`_ [VeC 77]: vlib: require main core with 'skip-cores' attribute
  | `40633 <https:////gerrit.fd.io/r/c/vpp/+/40633>`_ [VeC 116]: docs: update core-pinning configuration

**Ivan Shvedunov** <ivan4th@gmail.com>:

  | `39615 <https:////gerrit.fd.io/r/c/vpp/+/39615>`_ [Vec 158]: ip: fix crash in ip4_neighbor_advertise

**Jay Wang** <jay.wang2@arm.com>:

  | `40890 <https:////gerrit.fd.io/r/c/vpp/+/40890>`_ [VeC 33]: vlib: fix seed parse error
  | `41259 <https:////gerrit.fd.io/r/c/vpp/+/41259>`_ [VeC 45]: vppinfra: add ARM neoverse-v2 support

**Klement Sekera** <klement.sekera@gmail.com>:

  | `40839 <https:////gerrit.fd.io/r/c/vpp/+/40839>`_ [veC 63]: ip: add extended shallow reassembly
  | `40837 <https:////gerrit.fd.io/r/c/vpp/+/40837>`_ [VeC 63]: ip: fix ip4 shallow reassembly output feature handoff
  | `40838 <https:////gerrit.fd.io/r/c/vpp/+/40838>`_ [VeC 63]: ip: add ip6 shallow reassembly output feature
  | `40547 <https:////gerrit.fd.io/r/c/vpp/+/40547>`_ [VeC 160]: vapi: don't store dict in length field

**Konstantin Kogdenko** <k.kogdenko@gmail.com>:

  | `39518 <https:////gerrit.fd.io/r/c/vpp/+/39518>`_ [VeC 124]: linux-cp: Add VRF synchronization

**Lajos Katona** <katonalala@gmail.com>:

  | `40898 <https:////gerrit.fd.io/r/c/vpp/+/40898>`_ [VEc 0]: vxlan: move vxlan-gpe to a plugin
  | `40460 <https:////gerrit.fd.io/r/c/vpp/+/40460>`_ [vEc 0]: api: Refresh VPP API language with path background
  | `40471 <https:////gerrit.fd.io/r/c/vpp/+/40471>`_ [VEc 0]: docs: Add doc for API Trace Tools

**Lukas Stockner** <lstockner@genesiscloud.com>:

  | `41252 <https:////gerrit.fd.io/r/c/vpp/+/41252>`_ [VeC 39]: buffers: support disabling allocation per numa domain

**Manual Praying** <bobobo1618@gmail.com>:

  | `40573 <https:////gerrit.fd.io/r/c/vpp/+/40573>`_ [veC 116]: nat: Implement SNAT on hairpin NAT for TCP, UDP and ICMP.
  | `40750 <https:////gerrit.fd.io/r/c/vpp/+/40750>`_ [Vec 126]: dhcp: Update RA for prefixes inside DHCP-PD prefixes.

**Matthew Smith** <mgsmith@netgate.com>:

  | `40983 <https:////gerrit.fd.io/r/c/vpp/+/40983>`_ [Vec 67]: vapi: only wait if queue is empty

**Maxime Peim** <mpeim@cisco.com>:

  | `40918 <https:////gerrit.fd.io/r/c/vpp/+/40918>`_ [veC 96]: classify: add name to classify heap
  | `40888 <https:////gerrit.fd.io/r/c/vpp/+/40888>`_ [VeC 104]: pg: allow node unformat after hex data

**Monendra Singh Kushwaha** <kmonendra@marvell.com>:

  | `41459 <https:////gerrit.fd.io/r/c/vpp/+/41459>`_ [VEc 5]: dev: add support for vf device with vf_token
  | `41093 <https:////gerrit.fd.io/r/c/vpp/+/41093>`_ [Vec 77]: octeon: fix oct_free() and free allocated memory

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `32819 <https:////gerrit.fd.io/r/c/vpp/+/32819>`_ [VeC 161]: vlib: allow overlapping cli subcommands

**Neale Ranns** <neale@graphiant.com>:

  | `40288 <https:////gerrit.fd.io/r/c/vpp/+/40288>`_ [veC 146]: fib: Fix the make-before break load-balance construction

**Nikita Skrynnik** <nikita.skrynnik@xored.com>:

  | `40325 <https:////gerrit.fd.io/r/c/vpp/+/40325>`_ [Vec 158]: ping: Allow to specify a source interface in ping binary API
  | `40246 <https:////gerrit.fd.io/r/c/vpp/+/40246>`_ [VeC 166]: ping: Check only PING_RESPONSE_IP4 and PING_RESPONSE_IP6 events

**Nithinsen Kaithakadan** <nkaithakadan@marvell.com>:

  | `40548 <https:////gerrit.fd.io/r/c/vpp/+/40548>`_ [VeC 147]: octeon: add crypto framework

**Ole Troan** <otroan@employees.org>:

  | `41342 <https:////gerrit.fd.io/r/c/vpp/+/41342>`_ [VEc 12]: ip6: don't forward packets with invalid source address

**Oussama Drici** <o.drici@esi-sba.dz>:

  | `40488 <https:////gerrit.fd.io/r/c/vpp/+/40488>`_ [VeC 146]: bfd: move bfd to plugin, fix checkstyle, fix bfd test, bfd docs,

**Pierre Pfister** <ppfister@cisco.com>:

  | `40767 <https:////gerrit.fd.io/r/c/vpp/+/40767>`_ [VeC 75]: ipsec: add SA validity check fetching IPsec SA
  | `40760 <https:////gerrit.fd.io/r/c/vpp/+/40760>`_ [VeC 104]: vppinfra: fix dpdk compilation
  | `40758 <https:////gerrit.fd.io/r/c/vpp/+/40758>`_ [vec 111]: build: add config option for LD_PRELOAD

**Todd Hsiao** <thsiao@cisco.com>:

  | `40462 <https:////gerrit.fd.io/r/c/vpp/+/40462>`_ [veC 88]: ip: Full reassembly and fragmentation enhancement
  | `40992 <https:////gerrit.fd.io/r/c/vpp/+/40992>`_ [veC 88]: ip: add IPV6_FRAGMENTATION to extension_hdr_type

**Tom Jones** <thj@freebsd.org>:

  | `41354 <https:////gerrit.fd.io/r/c/vpp/+/41354>`_ [vEC 25]: dpdk: Enable dpdk build on FreeBSD

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `40626 <https:////gerrit.fd.io/r/c/vpp/+/40626>`_ [VEc 0]: ip6-nd: simplify API to directly set options

**Vladimir Zhigulin** <vladimir.jigulin@travelping.com>:

  | `40145 <https:////gerrit.fd.io/r/c/vpp/+/40145>`_ [VeC 129]: vppinfra: collect heap stats in constant time

**Vladislav Grishenko** <themiron@mail.ru>:

  | `41174 <https:////gerrit.fd.io/r/c/vpp/+/41174>`_ [VeC 65]: fib: fix fib entry tracking crash on table remove
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VeC 65]: fib: fix udp encap mp-safe ops and id validation
  | `40627 <https:////gerrit.fd.io/r/c/vpp/+/40627>`_ [VeC 66]: fib: fix invalid udp encap id cases
  | `40630 <https:////gerrit.fd.io/r/c/vpp/+/40630>`_ [VeC 95]: vlib: mark cli quit command as mp_safe
  | `40436 <https:////gerrit.fd.io/r/c/vpp/+/40436>`_ [Vec 139]: ip: mark IP_TABLE_DUMP and IP_ROUTE_DUMP as mp-safe
  | `40440 <https:////gerrit.fd.io/r/c/vpp/+/40440>`_ [VeC 144]: fib: add ip4 fib preallocation support
  | `35726 <https:////gerrit.fd.io/r/c/vpp/+/35726>`_ [VeC 144]: papi: fix socket api max message id calculation
  | `39579 <https:////gerrit.fd.io/r/c/vpp/+/39579>`_ [VeC 148]: fib: ensure mpls dpo index is valid for its next node
  | `40629 <https:////gerrit.fd.io/r/c/vpp/+/40629>`_ [VeC 148]: stats: add interface link speed to statseg
  | `40628 <https:////gerrit.fd.io/r/c/vpp/+/40628>`_ [VeC 148]: stats: add sw interface tags to statseg
  | `38524 <https:////gerrit.fd.io/r/c/vpp/+/38524>`_ [VeC 148]: fib: fix interface resolve from unlinked fib entries
  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [VeC 148]: mpls: fix crashes on mpls tunnel create/delete
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VeC 177]: nat: fix nat44-ed address removal from fib
  | `40413 <https:////gerrit.fd.io/r/c/vpp/+/40413>`_ [VeC 177]: nat: stick nat44-ed to use configured outside-fib

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `40666 <https:////gerrit.fd.io/r/c/vpp/+/40666>`_ [VeC 139]: ipsec: cli: 'set interface ipsec spd' support delete

**Zephyr Pellerin** <zpelleri@cisco.com>:

  | `40879 <https:////gerrit.fd.io/r/c/vpp/+/40879>`_ [VeC 104]: build: don't embed directives within macro arguments

**jinhui li** <lijh_7@chinatelecom.cn>:

  | `40717 <https:////gerrit.fd.io/r/c/vpp/+/40717>`_ [VeC 133]: ip: discard old trace flag after copy

**kai zhang** <zhangkaiheb@126.com>:

  | `40241 <https:////gerrit.fd.io/r/c/vpp/+/40241>`_ [veC 157]: dpdk: problem in parsing max-simd-bitwidth setting

**shaohui jin** <jinshaohui789@163.com>:

  | `39776 <https:////gerrit.fd.io/r/c/vpp/+/39776>`_ [VeC 166]: vppinfra: fix memory overrun in mhash_set_mem

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
authors          74
maintainers      23
committers       1
abandoned        0
================ ===

