
==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Thursday 2024-06-13, 02:07:07
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

  | `40767 <https:////gerrit.fd.io/r/c/vpp/+/40767>`_ [VECR 0]: ipsec: add SA validity check fetching IPsec SA

Maintainers:
------------
| **Please review these gerrit changes.**

| **NOTE: Gerrit changes may be included under more than one feature based on the modified files regardless of the feature list included on the commit headline.**

acl: **Andrew Yourtchenko** <ayourtch@gmail.com>
  | `41111 <https:////gerrit.fd.io/r/c/vpp/+/41111>`_ [VECr 1]: acl: cli addition to set macip rules

build: **Damjan Marion** <damarion@cisco.com>
  | `40920 <https:////gerrit.fd.io/r/c/vpp/+/40920>`_ [VECr 20]: tests: more options for decoding pcaps

builtinurl: **Dave Barach** <vpp@barachs.net>
  | `41076 <https:////gerrit.fd.io/r/c/vpp/+/41076>`_ [VECr 2]: http: return more than url to server app

crypto-openssl: **Damjan Marion** <damarion@cisco.com>
  | `41032 <https:////gerrit.fd.io/r/c/vpp/+/41032>`_ [VECr 0]: crypto: Add prefetching for src and dst

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `41076 <https:////gerrit.fd.io/r/c/vpp/+/41076>`_ [VECr 2]: http: return more than url to server app
  | `40890 <https:////gerrit.fd.io/r/c/vpp/+/40890>`_ [VECr 19]: vlib: fix seed parse error

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `40760 <https:////gerrit.fd.io/r/c/vpp/+/40760>`_ [VECr 29]: vppinfra: fix dpdk compilation

hash: **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>, **Damjan Marion** <damarion@cisco.com>
  | `41107 <https:////gerrit.fd.io/r/c/vpp/+/41107>`_ [VECr 1]: hash: Add cli to enable soft interface hashing based on esp

hs-test: **Florin Coras** <fcoras@cisco.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Maros Ondrejicka** <maros.ondrejicka@pantheon.tech>
  | `41076 <https:////gerrit.fd.io/r/c/vpp/+/41076>`_ [VECr 2]: http: return more than url to server app

hsa: **Florin Coras** <fcoras@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>
  | `41076 <https:////gerrit.fd.io/r/c/vpp/+/41076>`_ [VECr 2]: http: return more than url to server app

http: **Florin Coras** <fcoras@cisco.com>
  | `41076 <https:////gerrit.fd.io/r/c/vpp/+/41076>`_ [VECr 2]: http: return more than url to server app

http_static: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `41076 <https:////gerrit.fd.io/r/c/vpp/+/41076>`_ [VECr 2]: http: return more than url to server app

ikev2: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Benoît Ganne** <bganne@cisco.com>
  | `40400 <https:////gerrit.fd.io/r/c/vpp/+/40400>`_ [VECr 13]: ikev2: handoff packets
  | `40850 <https:////gerrit.fd.io/r/c/vpp/+/40850>`_ [VECr 30]: ikev2: multiple ts per profile

ioam: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `40898 <https:////gerrit.fd.io/r/c/vpp/+/40898>`_ [VECr 2]: vxlan: move vxlan-gpe to a plugin
  | `40879 <https:////gerrit.fd.io/r/c/vpp/+/40879>`_ [VECr 29]: build: don't embed directives within macro arguments

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `40839 <https:////gerrit.fd.io/r/c/vpp/+/40839>`_ [VECr 16]: ip: add extended shallow reassembly
  | `40837 <https:////gerrit.fd.io/r/c/vpp/+/40837>`_ [VECr 16]: ip: fix ip4 shallow reassembly output feature handoff
  | `40838 <https:////gerrit.fd.io/r/c/vpp/+/40838>`_ [VECr 16]: ip: add ip6 shallow reassembly output feature
  | `40927 <https:////gerrit.fd.io/r/c/vpp/+/40927>`_ [VECr 19]: ip6: fix ip6-michain trace function
  | `40879 <https:////gerrit.fd.io/r/c/vpp/+/40879>`_ [VECr 29]: build: don't embed directives within macro arguments

ipsec: **Neale Ranns** <neale@graphiant.com>, **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `41103 <https:////gerrit.fd.io/r/c/vpp/+/41103>`_ [VECr 0]: ipsec: Add api to show the number of SAs distributed over the workers

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `41107 <https:////gerrit.fd.io/r/c/vpp/+/41107>`_ [VECr 1]: hash: Add cli to enable soft interface hashing based on esp
  | `40898 <https:////gerrit.fd.io/r/c/vpp/+/40898>`_ [VECr 2]: vxlan: move vxlan-gpe to a plugin
  | `40839 <https:////gerrit.fd.io/r/c/vpp/+/40839>`_ [VECr 16]: ip: add extended shallow reassembly
  | `40837 <https:////gerrit.fd.io/r/c/vpp/+/40837>`_ [VECr 16]: ip: fix ip4 shallow reassembly output feature handoff

nsh: **Hongjun Ni** <hongjun.ni@intel.com>, **Vengada** <venggovi@cisco.com>
  | `40898 <https:////gerrit.fd.io/r/c/vpp/+/40898>`_ [VECr 2]: vxlan: move vxlan-gpe to a plugin

pg: **Dave Barach** <vpp@barachs.net>
  | `40888 <https:////gerrit.fd.io/r/c/vpp/+/40888>`_ [VECr 29]: pg: allow node unformat after hex data

tcp: **Florin Coras** <fcoras@cisco.com>
  | `41102 <https:////gerrit.fd.io/r/c/vpp/+/41102>`_ [VECr 2]: tcp: make syn-rcvd timeout configurable

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `40400 <https:////gerrit.fd.io/r/c/vpp/+/40400>`_ [VECr 13]: ikev2: handoff packets
  | `40920 <https:////gerrit.fd.io/r/c/vpp/+/40920>`_ [VECr 20]: tests: more options for decoding pcaps
  | `40711 <https:////gerrit.fd.io/r/c/vpp/+/40711>`_ [VECr 29]: vlib: fix automatic core pinning

vapi: **Ole Troan** <ot@cisco.com>
  | `41105 <https:////gerrit.fd.io/r/c/vpp/+/41105>`_ [VECr 1]: vapi: Add option to dispatch with timeout
  | `40983 <https:////gerrit.fd.io/r/c/vpp/+/40983>`_ [VECr 14]: vapi: only wait if queue is empty

vcl: **Florin Coras** <fcoras@cisco.com>
  | `40537 <https:////gerrit.fd.io/r/c/vpp/+/40537>`_ [VECr 12]: misc: patch to test CI infra changes

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `41099 <https:////gerrit.fd.io/r/c/vpp/+/41099>`_ [VECr 2]: vlib: require main core with 'skip-cores' attribute
  | `40890 <https:////gerrit.fd.io/r/c/vpp/+/40890>`_ [VECr 19]: vlib: fix seed parse error
  | `40630 <https:////gerrit.fd.io/r/c/vpp/+/40630>`_ [VECr 20]: vlib: mark cli quit command as mp_safe
  | `40711 <https:////gerrit.fd.io/r/c/vpp/+/40711>`_ [VECr 29]: vlib: fix automatic core pinning

vnet: **Damjan Marion** <damarion@cisco.com>
  | `40836 <https:////gerrit.fd.io/r/c/vpp/+/40836>`_ [VECr 16]: vnet: print Success for API errno 0 instead of UNKNOWN

vpp: **Dave Barach** <vpp@barachs.net>
  | `40711 <https:////gerrit.fd.io/r/c/vpp/+/40711>`_ [VECr 29]: vlib: fix automatic core pinning

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `40377 <https:////gerrit.fd.io/r/c/vpp/+/40377>`_ [VECr 0]: vppinfra: fix cpu freq init error if cpu support aperfmperf
  | `40994 <https:////gerrit.fd.io/r/c/vpp/+/40994>`_ [VECr 13]: vppinfra: fix huge page alloc error on 5.19+ kernel
  | `40711 <https:////gerrit.fd.io/r/c/vpp/+/40711>`_ [VECr 29]: vlib: fix automatic core pinning
  | `40848 <https:////gerrit.fd.io/r/c/vpp/+/40848>`_ [VECr 29]: vlib: resolving core affinity on platforms with more than 128 cpus

wireguard: **Artem Glazychev** <artem.glazychev@xored.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `40854 <https:////gerrit.fd.io/r/c/vpp/+/40854>`_ [VECr 27]: wireguard: fix dereference null return value
  | `40841 <https:////gerrit.fd.io/r/c/vpp/+/40841>`_ [VECr 29]: wireguard: fix uninitialized pointer read

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Adrian Villin** <avillin@cisco.com>:

  | `40720 <https:////gerrit.fd.io/r/c/vpp/+/40720>`_ [VeC 41]: ip: added CLI command to set ip6 reassembly params
  | `40073 <https:////gerrit.fd.io/r/c/vpp/+/40073>`_ [VeC 42]: tests: Added SRv6 End.Am behaviour test
  | `40721 <https:////gerrit.fd.io/r/c/vpp/+/40721>`_ [VeC 48]: tests: minor improvements to test_snort

**Alok Mishra** <almishra@marvell.com>:

  | `40823 <https:////gerrit.fd.io/r/c/vpp/+/40823>`_ [VEc 0]: octeon: add support for max_rx_frame_size update

**Aman Singh** <aman.deep.singh@intel.com>:

  | `40371 <https:////gerrit.fd.io/r/c/vpp/+/40371>`_ [Vec 111]: ipsec: notify key changes to crypto engine during sa update

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `39994 <https:////gerrit.fd.io/r/c/vpp/+/39994>`_ [vEc 0]: pvti: Packet Vector Tunnel Interface

**Arthur de Kerhor** <arthurdekerhor@gmail.com>:

  | `39532 <https:////gerrit.fd.io/r/c/vpp/+/39532>`_ [vec 175]: ena: add tx checksum offloads and tso support

**Bence Romsics** <bence.romsics@gmail.com>:

  | `40402 <https:////gerrit.fd.io/r/c/vpp/+/40402>`_ [VeC 43]: docs: Restore and update nat section of progressive tutorial

**Benoît Ganne** <bganne@cisco.com>:

  | `40746 <https:////gerrit.fd.io/r/c/vpp/+/40746>`_ [VeC 41]: fib: make mfib optional
  | `40745 <https:////gerrit.fd.io/r/c/vpp/+/40745>`_ [VeC 56]: fib: improve ipv6 fib scaling
  | `39525 <https:////gerrit.fd.io/r/c/vpp/+/39525>`_ [VeC 119]: fib: log an error when destroying non-empty tables

**Daniel Beres** <dberes@cisco.com>:

  | `37071 <https:////gerrit.fd.io/r/c/vpp/+/37071>`_ [Vec 175]: ebuild: adding libmemif to debian packages

**Dau Do** <daudo@yahoo.com>:

  | `41104 <https:////gerrit.fd.io/r/c/vpp/+/41104>`_ [vEC 1]: ipsec: Add option to configure the handoff worker queue size
  | `41100 <https:////gerrit.fd.io/r/c/vpp/+/41100>`_ [vEC 2]: ipsec: Add option to configure the handoff worker queue size
  | `40831 <https:////gerrit.fd.io/r/c/vpp/+/40831>`_ [veC 46]: ipsec: added CLI command to show the SA's distributed between workers. Added configuration option to adjust the worker queue size. Both of these are used for performance tune-up. In our setting, it's best to set a bigger queue size to avoid the congestion drop. If not set, it's default to current queue size.

**Dmitry Valter** <dvalter@protonmail.com>:

  | `40503 <https:////gerrit.fd.io/r/c/vpp/+/40503>`_ [VeC 32]: tests: skip more excluded plugin tests
  | `40082 <https:////gerrit.fd.io/r/c/vpp/+/40082>`_ [VeC 51]: ip: mark ipX_header_t and ip4_address_t as packed
  | `40697 <https:////gerrit.fd.io/r/c/vpp/+/40697>`_ [VeC 62]: fib: fix mpls tunnel restacking
  | `40478 <https:////gerrit.fd.io/r/c/vpp/+/40478>`_ [VeC 79]: vlib: add config for elog tracing
  | `40150 <https:////gerrit.fd.io/r/c/vpp/+/40150>`_ [VeC 159]: vppinfra: fix test_vec invalid checks
  | `40123 <https:////gerrit.fd.io/r/c/vpp/+/40123>`_ [VeC 175]: fib: fix ip drop path crashes
  | `40122 <https:////gerrit.fd.io/r/c/vpp/+/40122>`_ [VeC 176]: vppapigen: fix enum format function

**Emmanuel Scaria** <emmanuelscaria11@gmail.com>:

  | `40293 <https:////gerrit.fd.io/r/c/vpp/+/40293>`_ [Vec 126]: tcp: Start persist timer if snd_wnd is zero and no probing
  | `40129 <https:////gerrit.fd.io/r/c/vpp/+/40129>`_ [vec 173]: tcp: drop resets on tcp closed state Type: improvement Change-Id: If0318aa13a98ac4bdceca1b7f3b5d646b4b8d550 Signed-off-by: emmanuel <emmanuelscaria11@gmail.com>

**Florin Coras** <florin.coras@gmail.com>:

  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VeC 108]: session: make local port allocator fib aware

**Gabriel Oginski** <gabrielx.oginski@intel.com>:

  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VeC 177]: interface dpdk avf: introducing setting RSS hash key feature

**Hadi Dernaika** <hadidernaika31@gmail.com>:

  | `39995 <https:////gerrit.fd.io/r/c/vpp/+/39995>`_ [Vec 91]: virtio: fix crash on show tun cli

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `40633 <https:////gerrit.fd.io/r/c/vpp/+/40633>`_ [VeC 41]: docs: update core-pinning configuration
  | `40088 <https:////gerrit.fd.io/r/c/vpp/+/40088>`_ [Vec 58]: misc: move snap, llc, osi to plugin

**Ivan Shvedunov** <ivan4th@gmail.com>:

  | `39615 <https:////gerrit.fd.io/r/c/vpp/+/39615>`_ [Vec 83]: ip: fix crash in ip4_neighbor_advertise

**Klement Sekera** <klement.sekera@gmail.com>:

  | `40547 <https:////gerrit.fd.io/r/c/vpp/+/40547>`_ [VeC 85]: vapi: don't store dict in length field

**Konstantin Kogdenko** <k.kogdenko@gmail.com>:

  | `39518 <https:////gerrit.fd.io/r/c/vpp/+/39518>`_ [VeC 49]: linux-cp: Add VRF synchronization

**Lajos Katona** <katonalala@gmail.com>:

  | `40471 <https:////gerrit.fd.io/r/c/vpp/+/40471>`_ [VEc 1]: docs: Add doc for API Trace Tools
  | `40460 <https:////gerrit.fd.io/r/c/vpp/+/40460>`_ [vEc 2]: api: Refresh VPP API language with path background

**Manual Praying** <bobobo1618@gmail.com>:

  | `40573 <https:////gerrit.fd.io/r/c/vpp/+/40573>`_ [veC 41]: nat: Implement SNAT on hairpin NAT for TCP, UDP and ICMP.
  | `40750 <https:////gerrit.fd.io/r/c/vpp/+/40750>`_ [Vec 51]: dhcp: Update RA for prefixes inside DHCP-PD prefixes.

**Maxime Peim** <mpeim@cisco.com>:

  | `40918 <https:////gerrit.fd.io/r/c/vpp/+/40918>`_ [vEC 21]: classify: add name to classify heap
  | `40452 <https:////gerrit.fd.io/r/c/vpp/+/40452>`_ [VeC 61]: ip6: fix icmp error on check fail
  | `40368 <https:////gerrit.fd.io/r/c/vpp/+/40368>`_ [VeC 103]: fib: fix covered_inherit_add

**Monendra Singh Kushwaha** <kmonendra@marvell.com>:

  | `41093 <https:////gerrit.fd.io/r/c/vpp/+/41093>`_ [VEc 2]: octeon: fix oct_free() and free allocated memory

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `32819 <https:////gerrit.fd.io/r/c/vpp/+/32819>`_ [VeC 86]: vlib: allow overlapping cli subcommands

**Neale Ranns** <neale@graphiant.com>:

  | `40288 <https:////gerrit.fd.io/r/c/vpp/+/40288>`_ [veC 71]: fib: Fix the make-before break load-balance construction
  | `40360 <https:////gerrit.fd.io/r/c/vpp/+/40360>`_ [veC 112]: vlib: Drain the frame queues before pausing at barrier.     - thread hand-off puts buffer in a frame queue between workers x and y. if worker y is waiting for the barrier lock, then these buffers are not processed until the lock is released. At that point state referred to by the buffers (e.g. an IPSec SA or an RX interface) could have been removed. so drain the frame queues for all workers before claiming to have reached the barrier.     - getting to the barrier is changed to a staged approach, with actions taken at each stage.
  | `40361 <https:////gerrit.fd.io/r/c/vpp/+/40361>`_ [veC 115]: vlib: remove the now unrequired frame queue check count.    - there is now an accurate measure of whether frame queues are populated.

**Nick Zavaritsky** <nick.zavaritsky@emnify.com>:

  | `39477 <https:////gerrit.fd.io/r/c/vpp/+/39477>`_ [VeC 176]: geneve: support custom options in decap

**Nikita Skrynnik** <nikita.skrynnik@xored.com>:

  | `40325 <https:////gerrit.fd.io/r/c/vpp/+/40325>`_ [Vec 83]: ping: Allow to specify a source interface in ping binary API
  | `40246 <https:////gerrit.fd.io/r/c/vpp/+/40246>`_ [VeC 91]: ping: Check only PING_RESPONSE_IP4 and PING_RESPONSE_IP6 events

**Nithinsen Kaithakadan** <nkaithakadan@marvell.com>:

  | `40548 <https:////gerrit.fd.io/r/c/vpp/+/40548>`_ [VeC 72]: octeon: add crypto framework

**Oussama Drici** <o.drici@esi-sba.dz>:

  | `40488 <https:////gerrit.fd.io/r/c/vpp/+/40488>`_ [VeC 71]: bfd: move bfd to plugin, fix checkstyle, fix bfd test, bfd docs,

**Pierre Pfister** <ppfister@cisco.com>:

  | `40758 <https:////gerrit.fd.io/r/c/vpp/+/40758>`_ [vec 36]: build: add config option for LD_PRELOAD

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `40861 <https:////gerrit.fd.io/r/c/vpp/+/40861>`_ [VeC 32]: vapi: remove plugin dependency from tests
  | `40379 <https:////gerrit.fd.io/r/c/vpp/+/40379>`_ [VeC 110]: linux-cp: populate mapping vif-sw_if_index only for default-ns
  | `40292 <https:////gerrit.fd.io/r/c/vpp/+/40292>`_ [VeC 128]: tap: add virtio polling option

**Todd Hsiao** <thsiao@cisco.com>:

  | `40462 <https:////gerrit.fd.io/r/c/vpp/+/40462>`_ [vEC 13]: ip: Full reassembly and fragmentation enhancement
  | `40992 <https:////gerrit.fd.io/r/c/vpp/+/40992>`_ [vEC 13]: ip: add IPV6_FRAGMENTATION to extension_hdr_type

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `41096 <https:////gerrit.fd.io/r/c/vpp/+/41096>`_ [vEC 2]: dpdk: enumerate only net vmbus devices, don't use port_id
  | `40626 <https:////gerrit.fd.io/r/c/vpp/+/40626>`_ [VEc 8]: ip6-nd: simplify API to directly set options

**Vladimir Zhigulin** <vladimir.jigulin@travelping.com>:

  | `40145 <https:////gerrit.fd.io/r/c/vpp/+/40145>`_ [VeC 54]: vppinfra: collect heap stats in constant time

**Vladislav Grishenko** <themiron@mail.ru>:

  | `40415 <https:////gerrit.fd.io/r/c/vpp/+/40415>`_ [VEc 20]: ip: mark IP_ADDRESS_DUMP as mp-safe
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VeC 57]: fib: fix udp encap mp-safe ops and id validation
  | `40627 <https:////gerrit.fd.io/r/c/vpp/+/40627>`_ [VeC 62]: fib: fix invalid udp encap id cases
  | `40436 <https:////gerrit.fd.io/r/c/vpp/+/40436>`_ [Vec 64]: ip: mark IP_TABLE_DUMP and IP_ROUTE_DUMP as mp-safe
  | `40440 <https:////gerrit.fd.io/r/c/vpp/+/40440>`_ [VeC 69]: fib: add ip4 fib preallocation support
  | `35726 <https:////gerrit.fd.io/r/c/vpp/+/35726>`_ [VeC 69]: papi: fix socket api max message id calculation
  | `39579 <https:////gerrit.fd.io/r/c/vpp/+/39579>`_ [VeC 73]: fib: ensure mpls dpo index is valid for its next node
  | `40629 <https:////gerrit.fd.io/r/c/vpp/+/40629>`_ [VeC 73]: stats: add interface link speed to statseg
  | `40628 <https:////gerrit.fd.io/r/c/vpp/+/40628>`_ [VeC 73]: stats: add sw interface tags to statseg
  | `38524 <https:////gerrit.fd.io/r/c/vpp/+/38524>`_ [VeC 73]: fib: fix interface resolve from unlinked fib entries
  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [VeC 73]: mpls: fix crashes on mpls tunnel create/delete
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VeC 102]: nat: fix nat44-ed address removal from fib
  | `40413 <https:////gerrit.fd.io/r/c/vpp/+/40413>`_ [VeC 102]: nat: stick nat44-ed to use configured outside-fib

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `40666 <https:////gerrit.fd.io/r/c/vpp/+/40666>`_ [VeC 64]: ipsec: cli: 'set interface ipsec spd' support delete

**jinhui li** <lijh_7@chinatelecom.cn>:

  | `40717 <https:////gerrit.fd.io/r/c/vpp/+/40717>`_ [VeC 58]: ip: discard old trace flag after copy

**kai zhang** <zhangkaiheb@126.com>:

  | `40241 <https:////gerrit.fd.io/r/c/vpp/+/40241>`_ [veC 82]: dpdk: problem in parsing max-simd-bitwidth setting

**shaohui jin** <jinshaohui789@163.com>:

  | `39776 <https:////gerrit.fd.io/r/c/vpp/+/39776>`_ [VeC 91]: vppinfra: fix memory overrun in mhash_set_mem

**steven luong** <sluong@cisco.com>:

  | `40109 <https:////gerrit.fd.io/r/c/vpp/+/40109>`_ [VeC 125]: virtio: RSS support

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
authors          76
maintainers      30
committers       1
abandoned        0
================ ===

