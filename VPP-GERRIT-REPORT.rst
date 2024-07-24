
==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Wednesday 2024-07-24, 02:10:30
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

api: **Dave Barach** <vpp@barachs.net>
  | `41257 <https:////gerrit.fd.io/r/c/vpp/+/41257>`_ [VECr 11]: api: support api clients with real-time scheduling

buffers: **Damjan Marion** <damarion@cisco.com>, **Dave Barach** <vpp@barachs.net>
  | `41252 <https:////gerrit.fd.io/r/c/vpp/+/41252>`_ [VECr 5]: buffers: support disabling allocation per numa domain

build: **Damjan Marion** <damarion@cisco.com>
  | `40971 <https:////gerrit.fd.io/r/c/vpp/+/40971>`_ [VECr 0]: build: add SHA256 checksums for external downloaded dependencies
  | `41259 <https:////gerrit.fd.io/r/c/vpp/+/41259>`_ [VECr 11]: vppinfra: add ARM neoverse-v2 support

dhcp: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `41272 <https:////gerrit.fd.io/r/c/vpp/+/41272>`_ [VECr 6]: dhcp: fix buffer length after adding new option

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `41252 <https:////gerrit.fd.io/r/c/vpp/+/41252>`_ [VECr 5]: buffers: support disabling allocation per numa domain
  | `40890 <https:////gerrit.fd.io/r/c/vpp/+/40890>`_ [VECr 28]: vlib: fix seed parse error

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `41168 <https:////gerrit.fd.io/r/c/vpp/+/41168>`_ [VECr 28]: dpdk: xstats as symlinks

hs-test: **Florin Coras** <fcoras@cisco.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Maros Ondrejicka** <maros.ondrejicka@pantheon.tech>
  | `41205 <https:////gerrit.fd.io/r/c/vpp/+/41205>`_ [VECr 0]: hs-test: update envoy

ioam: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `40898 <https:////gerrit.fd.io/r/c/vpp/+/40898>`_ [VECr 5]: vxlan: move vxlan-gpe to a plugin

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `40720 <https:////gerrit.fd.io/r/c/vpp/+/40720>`_ [VECr 15]: ip: added CLI command to set ip6 reassembly params
  | `40837 <https:////gerrit.fd.io/r/c/vpp/+/40837>`_ [VECr 29]: ip: fix ip4 shallow reassembly output feature handoff
  | `40838 <https:////gerrit.fd.io/r/c/vpp/+/40838>`_ [VECr 29]: ip: add ip6 shallow reassembly output feature

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `40898 <https:////gerrit.fd.io/r/c/vpp/+/40898>`_ [VECr 5]: vxlan: move vxlan-gpe to a plugin
  | `40837 <https:////gerrit.fd.io/r/c/vpp/+/40837>`_ [VECr 29]: ip: fix ip4 shallow reassembly output feature handoff

nsh: **Hongjun Ni** <hongjun.ni@intel.com>, **Vengada** <venggovi@cisco.com>
  | `40898 <https:////gerrit.fd.io/r/c/vpp/+/40898>`_ [VECr 5]: vxlan: move vxlan-gpe to a plugin

pg: **Dave Barach** <vpp@barachs.net>
  | `41246 <https:////gerrit.fd.io/r/c/vpp/+/41246>`_ [VECr 5]: pg: fix offload offsets for ip4/6-input

session: **Florin Coras** <fcoras@cisco.com>
  | `41275 <https:////gerrit.fd.io/r/c/vpp/+/41275>`_ [VECr 0]: session: delete and add application namespace do not create the global session table

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `41275 <https:////gerrit.fd.io/r/c/vpp/+/41275>`_ [VECr 0]: session: delete and add application namespace do not create the global session table
  | `41272 <https:////gerrit.fd.io/r/c/vpp/+/41272>`_ [VECr 6]: dhcp: fix buffer length after adding new option

vat2: **Ole Troan** <ot@cisco.com>
  | `41277 <https:////gerrit.fd.io/r/c/vpp/+/41277>`_ [VECr 5]: vat2: fix -p in vat2 help text

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `41094 <https:////gerrit.fd.io/r/c/vpp/+/41094>`_ [VECr 11]: vlib: improve core pinning
  | `40890 <https:////gerrit.fd.io/r/c/vpp/+/40890>`_ [VECr 28]: vlib: fix seed parse error

vpp: **Dave Barach** <vpp@barachs.net>
  | `41094 <https:////gerrit.fd.io/r/c/vpp/+/41094>`_ [VECr 11]: vlib: improve core pinning

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `41259 <https:////gerrit.fd.io/r/c/vpp/+/41259>`_ [VECr 11]: vppinfra: add ARM neoverse-v2 support
  | `41094 <https:////gerrit.fd.io/r/c/vpp/+/41094>`_ [VECr 11]: vlib: improve core pinning

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Adrian Villin** <avillin@cisco.com>:

  | `41204 <https:////gerrit.fd.io/r/c/vpp/+/41204>`_ [vEC 0]: hs-test: check container state after startup

**Alexander Chernavin** <achernavin@netgate.com>:

  | `41161 <https:////gerrit.fd.io/r/c/vpp/+/41161>`_ [VEc 27]: bonding: make link state depend on active members

**Alok Mishra** <almishra@marvell.com>:

  | `40823 <https:////gerrit.fd.io/r/c/vpp/+/40823>`_ [VEc 7]: octeon: add support for max_rx_frame_size update

**Aman Singh** <aman.deep.singh@intel.com>:

  | `40371 <https:////gerrit.fd.io/r/c/vpp/+/40371>`_ [Vec 152]: ipsec: notify key changes to crypto engine during sa update

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `41203 <https:////gerrit.fd.io/r/c/vpp/+/41203>`_ [vEC 5]: acl: use ip4_preflen_to_mask instead of artisanal function
  | `39994 <https:////gerrit.fd.io/r/c/vpp/+/39994>`_ [vEc 15]: pvti: Packet Vector Tunnel Interface

**Bence Romsics** <bence.romsics@gmail.com>:

  | `40402 <https:////gerrit.fd.io/r/c/vpp/+/40402>`_ [VeC 84]: docs: Restore and update nat section of progressive tutorial

**Dau Do** <daudo@yahoo.com>:

  | `41138 <https:////gerrit.fd.io/r/c/vpp/+/41138>`_ [VeC 34]: ipsec: add binapi to set/get the SA's seq/replay_window
  | `41107 <https:////gerrit.fd.io/r/c/vpp/+/41107>`_ [Vec 38]: hash: Add cli to enable soft interface hashing based on esp
  | `41103 <https:////gerrit.fd.io/r/c/vpp/+/41103>`_ [VeC 41]: ipsec: Add api to show the number of SAs distributed over the workers
  | `41104 <https:////gerrit.fd.io/r/c/vpp/+/41104>`_ [veC 42]: ipsec: Add option to configure the handoff worker queue size
  | `41100 <https:////gerrit.fd.io/r/c/vpp/+/41100>`_ [veC 43]: ipsec: Add option to configure the handoff worker queue size
  | `40831 <https:////gerrit.fd.io/r/c/vpp/+/40831>`_ [veC 87]: ipsec: added CLI command to show the SA's distributed between workers. Added configuration option to adjust the worker queue size. Both of these are used for performance tune-up. In our setting, it's best to set a bigger queue size to avoid the congestion drop. If not set, it's default to current queue size.

**Dave Wallace** <dwallacelf@gmail.com>:

  | `41288 <https:////gerrit.fd.io/r/c/vpp/+/41288>`_ [vEC 0]: tests: update scapy to version 2.4.5
  | `40537 <https:////gerrit.fd.io/r/c/vpp/+/40537>`_ [vEC 1]: misc: patch to test CI infra changes

**Denys Haryachyy** <garyachy@gmail.com>:

  | `40850 <https:////gerrit.fd.io/r/c/vpp/+/40850>`_ [VeC 71]: ikev2: multiple ts per profile

**Dmitry Valter** <dvalter@protonmail.com>:

  | `40122 <https:////gerrit.fd.io/r/c/vpp/+/40122>`_ [VeC 40]: vppapigen: fix enum format function
  | `40082 <https:////gerrit.fd.io/r/c/vpp/+/40082>`_ [VeC 92]: ip: mark ipX_header_t and ip4_address_t as packed
  | `40697 <https:////gerrit.fd.io/r/c/vpp/+/40697>`_ [VeC 103]: fib: fix mpls tunnel restacking
  | `40478 <https:////gerrit.fd.io/r/c/vpp/+/40478>`_ [VeC 120]: vlib: add config for elog tracing

**Emmanuel Scaria** <emmanuelscaria11@gmail.com>:

  | `40293 <https:////gerrit.fd.io/r/c/vpp/+/40293>`_ [Vec 167]: tcp: Start persist timer if snd_wnd is zero and no probing

**Florin Coras** <florin.coras@gmail.com>:

  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VeC 149]: session: make local port allocator fib aware

**Guillaume Solignac** <gsoligna@cisco.com>:

  | `41160 <https:////gerrit.fd.io/r/c/vpp/+/41160>`_ [VeC 34]: vppinfra: cleaner way of getting libdl in CMake

**Hadi Dernaika** <hadidernaika31@gmail.com>:

  | `39995 <https:////gerrit.fd.io/r/c/vpp/+/39995>`_ [Vec 132]: virtio: fix crash on show tun cli

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `41099 <https:////gerrit.fd.io/r/c/vpp/+/41099>`_ [VeC 43]: vlib: require main core with 'skip-cores' attribute
  | `40711 <https:////gerrit.fd.io/r/c/vpp/+/40711>`_ [VeC 70]: vlib: fix automatic core pinning
  | `40633 <https:////gerrit.fd.io/r/c/vpp/+/40633>`_ [VeC 82]: docs: update core-pinning configuration
  | `40088 <https:////gerrit.fd.io/r/c/vpp/+/40088>`_ [Vec 99]: misc: move snap, llc, osi to plugin

**Ivan Shvedunov** <ivan4th@gmail.com>:

  | `39615 <https:////gerrit.fd.io/r/c/vpp/+/39615>`_ [Vec 124]: ip: fix crash in ip4_neighbor_advertise

**Klement Sekera** <klement.sekera@gmail.com>:

  | `40839 <https:////gerrit.fd.io/r/c/vpp/+/40839>`_ [vEC 29]: ip: add extended shallow reassembly
  | `40547 <https:////gerrit.fd.io/r/c/vpp/+/40547>`_ [VeC 126]: vapi: don't store dict in length field

**Konstantin Kogdenko** <k.kogdenko@gmail.com>:

  | `39518 <https:////gerrit.fd.io/r/c/vpp/+/39518>`_ [VeC 90]: linux-cp: Add VRF synchronization

**Lajos Katona** <katonalala@gmail.com>:

  | `40460 <https:////gerrit.fd.io/r/c/vpp/+/40460>`_ [VEc 14]: api: Refresh VPP API language with path background
  | `40471 <https:////gerrit.fd.io/r/c/vpp/+/40471>`_ [VEc 14]: docs: Add doc for API Trace Tools

**Manual Praying** <bobobo1618@gmail.com>:

  | `40573 <https:////gerrit.fd.io/r/c/vpp/+/40573>`_ [veC 82]: nat: Implement SNAT on hairpin NAT for TCP, UDP and ICMP.
  | `40750 <https:////gerrit.fd.io/r/c/vpp/+/40750>`_ [Vec 92]: dhcp: Update RA for prefixes inside DHCP-PD prefixes.

**Matthew Smith** <mgsmith@netgate.com>:

  | `40983 <https:////gerrit.fd.io/r/c/vpp/+/40983>`_ [Vec 33]: vapi: only wait if queue is empty

**Matus Fabian** <matfabia@cisco.com>:

  | `41250 <https:////gerrit.fd.io/r/c/vpp/+/41250>`_ [VEc 0]: http_static: fix coverity warning
  | `41260 <https:////gerrit.fd.io/r/c/vpp/+/41260>`_ [vEC 0]: http: client code improvement

**Maxime Peim** <mpeim@cisco.com>:

  | `40918 <https:////gerrit.fd.io/r/c/vpp/+/40918>`_ [veC 62]: classify: add name to classify heap
  | `40888 <https:////gerrit.fd.io/r/c/vpp/+/40888>`_ [VeC 70]: pg: allow node unformat after hex data

**Monendra Singh Kushwaha** <kmonendra@marvell.com>:

  | `41093 <https:////gerrit.fd.io/r/c/vpp/+/41093>`_ [Vec 43]: octeon: fix oct_free() and free allocated memory

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `32819 <https:////gerrit.fd.io/r/c/vpp/+/32819>`_ [VeC 127]: vlib: allow overlapping cli subcommands

**Neale Ranns** <neale@graphiant.com>:

  | `40288 <https:////gerrit.fd.io/r/c/vpp/+/40288>`_ [veC 112]: fib: Fix the make-before break load-balance construction
  | `40360 <https:////gerrit.fd.io/r/c/vpp/+/40360>`_ [veC 153]: vlib: Drain the frame queues before pausing at barrier.     - thread hand-off puts buffer in a frame queue between workers x and y. if worker y is waiting for the barrier lock, then these buffers are not processed until the lock is released. At that point state referred to by the buffers (e.g. an IPSec SA or an RX interface) could have been removed. so drain the frame queues for all workers before claiming to have reached the barrier.     - getting to the barrier is changed to a staged approach, with actions taken at each stage.
  | `40361 <https:////gerrit.fd.io/r/c/vpp/+/40361>`_ [veC 156]: vlib: remove the now unrequired frame queue check count.    - there is now an accurate measure of whether frame queues are populated.

**Nikita Skrynnik** <nikita.skrynnik@xored.com>:

  | `40325 <https:////gerrit.fd.io/r/c/vpp/+/40325>`_ [Vec 124]: ping: Allow to specify a source interface in ping binary API
  | `40246 <https:////gerrit.fd.io/r/c/vpp/+/40246>`_ [VeC 132]: ping: Check only PING_RESPONSE_IP4 and PING_RESPONSE_IP6 events

**Nithinsen Kaithakadan** <nkaithakadan@marvell.com>:

  | `40548 <https:////gerrit.fd.io/r/c/vpp/+/40548>`_ [VeC 113]: octeon: add crypto framework

**Oussama Drici** <o.drici@esi-sba.dz>:

  | `40488 <https:////gerrit.fd.io/r/c/vpp/+/40488>`_ [VeC 112]: bfd: move bfd to plugin, fix checkstyle, fix bfd test, bfd docs,

**Pierre Pfister** <ppfister@cisco.com>:

  | `40767 <https:////gerrit.fd.io/r/c/vpp/+/40767>`_ [VeC 41]: ipsec: add SA validity check fetching IPsec SA
  | `40760 <https:////gerrit.fd.io/r/c/vpp/+/40760>`_ [VeC 70]: vppinfra: fix dpdk compilation
  | `40758 <https:////gerrit.fd.io/r/c/vpp/+/40758>`_ [vec 77]: build: add config option for LD_PRELOAD

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `40400 <https:////gerrit.fd.io/r/c/vpp/+/40400>`_ [VeC 54]: ikev2: handoff packets
  | `40861 <https:////gerrit.fd.io/r/c/vpp/+/40861>`_ [VeC 73]: vapi: remove plugin dependency from tests
  | `40292 <https:////gerrit.fd.io/r/c/vpp/+/40292>`_ [VeC 169]: tap: add virtio polling option

**Todd Hsiao** <thsiao@cisco.com>:

  | `40462 <https:////gerrit.fd.io/r/c/vpp/+/40462>`_ [veC 54]: ip: Full reassembly and fragmentation enhancement
  | `40992 <https:////gerrit.fd.io/r/c/vpp/+/40992>`_ [veC 54]: ip: add IPV6_FRAGMENTATION to extension_hdr_type

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `40626 <https:////gerrit.fd.io/r/c/vpp/+/40626>`_ [VEc 28]: ip6-nd: simplify API to directly set options

**Vladimir Zhigulin** <vladimir.jigulin@travelping.com>:

  | `40145 <https:////gerrit.fd.io/r/c/vpp/+/40145>`_ [VeC 95]: vppinfra: collect heap stats in constant time

**Vladislav Grishenko** <themiron@mail.ru>:

  | `41174 <https:////gerrit.fd.io/r/c/vpp/+/41174>`_ [VeC 31]: fib: fix fib entry tracking crash on table remove
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VeC 31]: fib: fix udp encap mp-safe ops and id validation
  | `40627 <https:////gerrit.fd.io/r/c/vpp/+/40627>`_ [VeC 32]: fib: fix invalid udp encap id cases
  | `40630 <https:////gerrit.fd.io/r/c/vpp/+/40630>`_ [VeC 61]: vlib: mark cli quit command as mp_safe
  | `40436 <https:////gerrit.fd.io/r/c/vpp/+/40436>`_ [Vec 105]: ip: mark IP_TABLE_DUMP and IP_ROUTE_DUMP as mp-safe
  | `40440 <https:////gerrit.fd.io/r/c/vpp/+/40440>`_ [VeC 110]: fib: add ip4 fib preallocation support
  | `35726 <https:////gerrit.fd.io/r/c/vpp/+/35726>`_ [VeC 110]: papi: fix socket api max message id calculation
  | `39579 <https:////gerrit.fd.io/r/c/vpp/+/39579>`_ [VeC 114]: fib: ensure mpls dpo index is valid for its next node
  | `40629 <https:////gerrit.fd.io/r/c/vpp/+/40629>`_ [VeC 114]: stats: add interface link speed to statseg
  | `40628 <https:////gerrit.fd.io/r/c/vpp/+/40628>`_ [VeC 114]: stats: add sw interface tags to statseg
  | `38524 <https:////gerrit.fd.io/r/c/vpp/+/38524>`_ [VeC 114]: fib: fix interface resolve from unlinked fib entries
  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [VeC 114]: mpls: fix crashes on mpls tunnel create/delete
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VeC 143]: nat: fix nat44-ed address removal from fib
  | `40413 <https:////gerrit.fd.io/r/c/vpp/+/40413>`_ [VeC 143]: nat: stick nat44-ed to use configured outside-fib

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `40666 <https:////gerrit.fd.io/r/c/vpp/+/40666>`_ [VeC 105]: ipsec: cli: 'set interface ipsec spd' support delete

**Zephyr Pellerin** <zpelleri@cisco.com>:

  | `40879 <https:////gerrit.fd.io/r/c/vpp/+/40879>`_ [VeC 70]: build: don't embed directives within macro arguments

**jinhui li** <lijh_7@chinatelecom.cn>:

  | `40717 <https:////gerrit.fd.io/r/c/vpp/+/40717>`_ [VeC 99]: ip: discard old trace flag after copy

**kai zhang** <zhangkaiheb@126.com>:

  | `40241 <https:////gerrit.fd.io/r/c/vpp/+/40241>`_ [veC 123]: dpdk: problem in parsing max-simd-bitwidth setting

**shaohui jin** <jinshaohui789@163.com>:

  | `39776 <https:////gerrit.fd.io/r/c/vpp/+/39776>`_ [VeC 132]: vppinfra: fix memory overrun in mhash_set_mem

**steven luong** <sluong@cisco.com>:

  | `40109 <https:////gerrit.fd.io/r/c/vpp/+/40109>`_ [VeC 166]: virtio: RSS support

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
authors          80
maintainers      16
committers       0
abandoned        0
================ ===

