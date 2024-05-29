
==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Wednesday 2024-05-29, 02:07:06
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

  | `40767 <https:////gerrit.fd.io/r/c/vpp/+/40767>`_ [VECR 5]: ipsec: add SA validity check fetching IPsec SA
  | `40823 <https:////gerrit.fd.io/r/c/vpp/+/40823>`_ [VECR 5]: octeon: add support for max_rx_frame_size update
  | `40503 <https:////gerrit.fd.io/r/c/vpp/+/40503>`_ [VECR 17]: tests: skip more excluded plugin tests

Maintainers:
------------
| **Please review these gerrit changes.**

| **NOTE: Gerrit changes may be included under more than one feature based on the modified files regardless of the feature list included on the commit headline.**

build: **Damjan Marion** <damarion@cisco.com>
  | `40177 <https:////gerrit.fd.io/r/c/vpp/+/40177>`_ [VECr 4]: hs-test: added targets to makefiles to get coverage from HS tests
  | `40920 <https:////gerrit.fd.io/r/c/vpp/+/40920>`_ [VECr 5]: tests: more options for decoding pcaps

dev: **Damjan Marion** <damarion@cisco.com>
  | `40904 <https:////gerrit.fd.io/r/c/vpp/+/40904>`_ [VECr 6]: dev: add port counter clear operation
  | `40892 <https:////gerrit.fd.io/r/c/vpp/+/40892>`_ [VECr 12]: dev: fix counter_start in counter clear routine

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `40890 <https:////gerrit.fd.io/r/c/vpp/+/40890>`_ [VECr 4]: vlib: fix seed parse error
  | `40633 <https:////gerrit.fd.io/r/c/vpp/+/40633>`_ [VECr 26]: docs: update core-pinning configuration
  | `40402 <https:////gerrit.fd.io/r/c/vpp/+/40402>`_ [VECr 28]: docs: Restore and update nat section of progressive tutorial

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `40760 <https:////gerrit.fd.io/r/c/vpp/+/40760>`_ [VECr 14]: vppinfra: fix dpdk compilation

fib: **Neale Ranns** <neale@graphiant.com>
  | `40718 <https:////gerrit.fd.io/r/c/vpp/+/40718>`_ [VECr 0]: fib: set the value of the sw_if_index for DROP route
  | `40719 <https:////gerrit.fd.io/r/c/vpp/+/40719>`_ [VECr 0]: ip: add support for drop route through vpp CLI

hs-test: **Florin Coras** <fcoras@cisco.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Maros Ondrejicka** <maros.ondrejicka@pantheon.tech>
  | `40956 <https:////gerrit.fd.io/r/c/vpp/+/40956>`_ [VECr 0]: hs-test: pin CPUs to containers
  | `40177 <https:////gerrit.fd.io/r/c/vpp/+/40177>`_ [VECr 4]: hs-test: added targets to makefiles to get coverage from HS tests
  | `40727 <https:////gerrit.fd.io/r/c/vpp/+/40727>`_ [VECr 5]: hs-test: break TcpWithLoss (unstable)

ikev2: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Benoît Ganne** <bganne@cisco.com>
  | `40400 <https:////gerrit.fd.io/r/c/vpp/+/40400>`_ [VECr 0]: ikev2: handoff packets
  | `40850 <https:////gerrit.fd.io/r/c/vpp/+/40850>`_ [VECr 15]: ikev2: multiple ts per profile

interface: **Dave Barach** <vpp@barachs.net>
  | `40746 <https:////gerrit.fd.io/r/c/vpp/+/40746>`_ [VECr 26]: fib: make mfib optional

ioam: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `40898 <https:////gerrit.fd.io/r/c/vpp/+/40898>`_ [VECr 1]: vxlan: move vxlan-gpe to a plugin
  | `40879 <https:////gerrit.fd.io/r/c/vpp/+/40879>`_ [VECr 14]: build: don't embed directives within macro arguments

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `40719 <https:////gerrit.fd.io/r/c/vpp/+/40719>`_ [VECr 0]: ip: add support for drop route through vpp CLI
  | `40839 <https:////gerrit.fd.io/r/c/vpp/+/40839>`_ [VECr 1]: ip: add extended shallow reassembly
  | `40837 <https:////gerrit.fd.io/r/c/vpp/+/40837>`_ [VECr 1]: ip: fix ip4 shallow reassembly output feature handoff
  | `40838 <https:////gerrit.fd.io/r/c/vpp/+/40838>`_ [VECr 1]: ip: add ip6 shallow reassembly output feature
  | `40927 <https:////gerrit.fd.io/r/c/vpp/+/40927>`_ [VECr 4]: ip6: fix ip6-michain trace function
  | `40879 <https:////gerrit.fd.io/r/c/vpp/+/40879>`_ [VECr 14]: build: don't embed directives within macro arguments
  | `40720 <https:////gerrit.fd.io/r/c/vpp/+/40720>`_ [VECr 26]: ip: added CLI command to set ip6 reassembly params
  | `40746 <https:////gerrit.fd.io/r/c/vpp/+/40746>`_ [VECr 26]: fib: make mfib optional

ipsec: **Neale Ranns** <neale@graphiant.com>, **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `39979 <https:////gerrit.fd.io/r/c/vpp/+/39979>`_ [VECr 13]: ipsec: move ah packet processing in the inline function ipsec_ah_packet_process
  | `40832 <https:////gerrit.fd.io/r/c/vpp/+/40832>`_ [VECr 29]: ipsec: added CLI command to show the SA's distributed between workers. Added configuration option to adjust the worker queue size. Both of these are used for performance tune-up. In our setting, it's best to set a bigger queue size to avoid the congestion drop. If not set, it's default to current queue size.

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `40839 <https:////gerrit.fd.io/r/c/vpp/+/40839>`_ [VECr 1]: ip: add extended shallow reassembly
  | `40837 <https:////gerrit.fd.io/r/c/vpp/+/40837>`_ [VECr 1]: ip: fix ip4 shallow reassembly output feature handoff
  | `40898 <https:////gerrit.fd.io/r/c/vpp/+/40898>`_ [VECr 1]: vxlan: move vxlan-gpe to a plugin

nsh: **Hongjun Ni** <hongjun.ni@intel.com>, **Vengada** <venggovi@cisco.com>
  | `40898 <https:////gerrit.fd.io/r/c/vpp/+/40898>`_ [VECr 1]: vxlan: move vxlan-gpe to a plugin

octeon: **Monendra Singh Kushwaha** <kmonendra@marvell.com>, **Damjan Marion** <damarion@cisco.com>
  | `40905 <https:////gerrit.fd.io/r/c/vpp/+/40905>`_ [VECr 7]: octeon: add clear counters support for port
  | `40893 <https:////gerrit.fd.io/r/c/vpp/+/40893>`_ [VECr 12]: octeon: add counters support for port and queue

pg: **Dave Barach** <vpp@barachs.net>
  | `40888 <https:////gerrit.fd.io/r/c/vpp/+/40888>`_ [VECr 14]: pg: allow node unformat after hex data

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `40400 <https:////gerrit.fd.io/r/c/vpp/+/40400>`_ [VECr 0]: ikev2: handoff packets
  | `40718 <https:////gerrit.fd.io/r/c/vpp/+/40718>`_ [VECr 0]: fib: set the value of the sw_if_index for DROP route
  | `40177 <https:////gerrit.fd.io/r/c/vpp/+/40177>`_ [VECr 4]: hs-test: added targets to makefiles to get coverage from HS tests
  | `40920 <https:////gerrit.fd.io/r/c/vpp/+/40920>`_ [VECr 5]: tests: more options for decoding pcaps
  | `40711 <https:////gerrit.fd.io/r/c/vpp/+/40711>`_ [VECr 14]: vlib: fix automatic core pinning
  | `40746 <https:////gerrit.fd.io/r/c/vpp/+/40746>`_ [VECr 26]: fib: make mfib optional
  | `40201 <https:////gerrit.fd.io/r/c/vpp/+/40201>`_ [VECr 27]: tests: organize test coverage report generation
  | `40073 <https:////gerrit.fd.io/r/c/vpp/+/40073>`_ [VECr 27]: tests: Added SRv6 End.Am behaviour test

unittest: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `40746 <https:////gerrit.fd.io/r/c/vpp/+/40746>`_ [VECr 26]: fib: make mfib optional

vapi: **Ole Troan** <ot@cisco.com>
  | `40983 <https:////gerrit.fd.io/r/c/vpp/+/40983>`_ [VECr 0]: vapi: only wait if queue is empty
  | `40861 <https:////gerrit.fd.io/r/c/vpp/+/40861>`_ [VECr 17]: vapi: remove plugin dependency from tests

vcl: **Florin Coras** <fcoras@cisco.com>
  | `40537 <https:////gerrit.fd.io/r/c/vpp/+/40537>`_ [VECr 29]: misc: patch to test CI infra changes

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `40890 <https:////gerrit.fd.io/r/c/vpp/+/40890>`_ [VECr 4]: vlib: fix seed parse error
  | `40630 <https:////gerrit.fd.io/r/c/vpp/+/40630>`_ [VECr 5]: vlib: mark cli quit command as mp_safe
  | `40711 <https:////gerrit.fd.io/r/c/vpp/+/40711>`_ [VECr 14]: vlib: fix automatic core pinning

vnet: **Damjan Marion** <damarion@cisco.com>
  | `40836 <https:////gerrit.fd.io/r/c/vpp/+/40836>`_ [VECr 1]: vnet: print Success for API errno 0 instead of UNKNOWN

vpp: **Dave Barach** <vpp@barachs.net>
  | `40711 <https:////gerrit.fd.io/r/c/vpp/+/40711>`_ [VECr 14]: vlib: fix automatic core pinning

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `40711 <https:////gerrit.fd.io/r/c/vpp/+/40711>`_ [VECr 14]: vlib: fix automatic core pinning
  | `40848 <https:////gerrit.fd.io/r/c/vpp/+/40848>`_ [VECr 14]: vlib: resolving core affinity on platforms with more than 128 cpus

wireguard: **Artem Glazychev** <artem.glazychev@xored.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `40854 <https:////gerrit.fd.io/r/c/vpp/+/40854>`_ [VECr 12]: wireguard: fix dereference null return value
  | `40841 <https:////gerrit.fd.io/r/c/vpp/+/40841>`_ [VECr 14]: wireguard: fix uninitialized pointer read

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Adrian Villin** <avillin@cisco.com>:

  | `40728 <https:////gerrit.fd.io/r/c/vpp/+/40728>`_ [vEC 5]: hs-test: break VCL tests (timeout)
  | `40726 <https:////gerrit.fd.io/r/c/vpp/+/40726>`_ [vEC 5]: hs-test: breaks HttpCliTest
  | `40721 <https:////gerrit.fd.io/r/c/vpp/+/40721>`_ [VeC 33]: tests: minor improvements to test_snort

**Aman Singh** <aman.deep.singh@intel.com>:

  | `40371 <https:////gerrit.fd.io/r/c/vpp/+/40371>`_ [Vec 96]: ipsec: notify key changes to crypto engine during sa update

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `39994 <https:////gerrit.fd.io/r/c/vpp/+/39994>`_ [vEc 13]: pvti: Packet Vector Tunnel Interface

**Arthur de Kerhor** <arthurdekerhor@gmail.com>:

  | `39532 <https:////gerrit.fd.io/r/c/vpp/+/39532>`_ [vec 160]: ena: add tx checksum offloads and tso support

**Benoît Ganne** <bganne@cisco.com>:

  | `40745 <https:////gerrit.fd.io/r/c/vpp/+/40745>`_ [VeC 41]: fib: improve ipv6 fib scaling
  | `39525 <https:////gerrit.fd.io/r/c/vpp/+/39525>`_ [VeC 104]: fib: log an error when destroying non-empty tables

**Damjan Marion** <dmarion@0xa5.net>:

  | `40929 <https:////gerrit.fd.io/r/c/vpp/+/40929>`_ [VEc 0]: vlib: stack trace and signal handler improvements

**Daniel Beres** <dberes@cisco.com>:

  | `37071 <https:////gerrit.fd.io/r/c/vpp/+/37071>`_ [Vec 160]: ebuild: adding libmemif to debian packages

**Dau Do** <daudo@yahoo.com>:

  | `40831 <https:////gerrit.fd.io/r/c/vpp/+/40831>`_ [veC 31]: ipsec: added CLI command to show the SA's distributed between workers. Added configuration option to adjust the worker queue size. Both of these are used for performance tune-up. In our setting, it's best to set a bigger queue size to avoid the congestion drop. If not set, it's default to current queue size.

**Dmitry Valter** <dvalter@protonmail.com>:

  | `40082 <https:////gerrit.fd.io/r/c/vpp/+/40082>`_ [VeC 36]: ip: mark ipX_header_t and ip4_address_t as packed
  | `40697 <https:////gerrit.fd.io/r/c/vpp/+/40697>`_ [VeC 47]: fib: fix mpls tunnel restacking
  | `40478 <https:////gerrit.fd.io/r/c/vpp/+/40478>`_ [VeC 64]: vlib: add config for elog tracing
  | `40150 <https:////gerrit.fd.io/r/c/vpp/+/40150>`_ [VeC 144]: vppinfra: fix test_vec invalid checks
  | `40123 <https:////gerrit.fd.io/r/c/vpp/+/40123>`_ [VeC 160]: fib: fix ip drop path crashes
  | `40122 <https:////gerrit.fd.io/r/c/vpp/+/40122>`_ [VeC 161]: vppapigen: fix enum format function
  | `40081 <https:////gerrit.fd.io/r/c/vpp/+/40081>`_ [VeC 173]: nat: fix det44 flaky test

**Emmanuel Scaria** <emmanuelscaria11@gmail.com>:

  | `40293 <https:////gerrit.fd.io/r/c/vpp/+/40293>`_ [Vec 111]: tcp: Start persist timer if snd_wnd is zero and no probing
  | `40129 <https:////gerrit.fd.io/r/c/vpp/+/40129>`_ [vec 158]: tcp: drop resets on tcp closed state Type: improvement Change-Id: If0318aa13a98ac4bdceca1b7f3b5d646b4b8d550 Signed-off-by: emmanuel <emmanuelscaria11@gmail.com>

**Fan Zhang** <fanzhang.oss@gmail.com>:

  | `40928 <https:////gerrit.fd.io/r/c/vpp/+/40928>`_ [vEc 0]: ipsec: fix missing udp port check

**Florin Coras** <florin.coras@gmail.com>:

  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VeC 93]: session: make local port allocator fib aware

**Gabriel Oginski** <gabrielx.oginski@intel.com>:

  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VeC 162]: interface dpdk avf: introducing setting RSS hash key feature

**Hadi Dernaika** <hadidernaika31@gmail.com>:

  | `39995 <https:////gerrit.fd.io/r/c/vpp/+/39995>`_ [Vec 76]: virtio: fix crash on show tun cli

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `40088 <https:////gerrit.fd.io/r/c/vpp/+/40088>`_ [Vec 43]: misc: move snap, llc, osi to plugin

**Ivan Shvedunov** <ivan4th@gmail.com>:

  | `39615 <https:////gerrit.fd.io/r/c/vpp/+/39615>`_ [Vec 68]: ip: fix crash in ip4_neighbor_advertise

**Klement Sekera** <klement.sekera@gmail.com>:

  | `40622 <https:////gerrit.fd.io/r/c/vpp/+/40622>`_ [VeC 60]: papi: more detailed packing error message
  | `40547 <https:////gerrit.fd.io/r/c/vpp/+/40547>`_ [VeC 70]: vapi: don't store dict in length field

**Konstantin Kogdenko** <k.kogdenko@gmail.com>:

  | `39518 <https:////gerrit.fd.io/r/c/vpp/+/39518>`_ [VeC 34]: linux-cp: Add VRF synchronization
  | `40280 <https:////gerrit.fd.io/r/c/vpp/+/40280>`_ [veC 87]: nat: add in2out-ip-fib-index config option

**Lajos Katona** <katonalala@gmail.com>:

  | `40460 <https:////gerrit.fd.io/r/c/vpp/+/40460>`_ [VEc 1]: api: Refresh VPP API language with path background
  | `40471 <https:////gerrit.fd.io/r/c/vpp/+/40471>`_ [VEc 1]: docs: Add doc for API Trace Tools

**Manual Praying** <bobobo1618@gmail.com>:

  | `40573 <https:////gerrit.fd.io/r/c/vpp/+/40573>`_ [vEC 26]: nat: Implement SNAT on hairpin NAT for TCP, UDP and ICMP.
  | `40750 <https:////gerrit.fd.io/r/c/vpp/+/40750>`_ [Vec 36]: dhcp: Update RA for prefixes inside DHCP-PD prefixes.

**Maxime Peim** <mpeim@cisco.com>:

  | `40918 <https:////gerrit.fd.io/r/c/vpp/+/40918>`_ [vEC 6]: classify: add name to classify heap
  | `40452 <https:////gerrit.fd.io/r/c/vpp/+/40452>`_ [VeC 46]: ip6: fix icmp error on check fail
  | `40368 <https:////gerrit.fd.io/r/c/vpp/+/40368>`_ [VeC 88]: fib: fix covered_inherit_add

**Monendra Singh Kushwaha** <kmonendra@marvell.com>:

  | `40914 <https:////gerrit.fd.io/r/c/vpp/+/40914>`_ [vEC 1]: octeon: update trace for flow redirection

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `32819 <https:////gerrit.fd.io/r/c/vpp/+/32819>`_ [VeC 71]: vlib: allow overlapping cli subcommands

**Neale Ranns** <neale@graphiant.com>:

  | `40288 <https:////gerrit.fd.io/r/c/vpp/+/40288>`_ [veC 56]: fib: Fix the make-before break load-balance construction
  | `40360 <https:////gerrit.fd.io/r/c/vpp/+/40360>`_ [veC 97]: vlib: Drain the frame queues before pausing at barrier.     - thread hand-off puts buffer in a frame queue between workers x and y. if worker y is waiting for the barrier lock, then these buffers are not processed until the lock is released. At that point state referred to by the buffers (e.g. an IPSec SA or an RX interface) could have been removed. so drain the frame queues for all workers before claiming to have reached the barrier.     - getting to the barrier is changed to a staged approach, with actions taken at each stage.
  | `40361 <https:////gerrit.fd.io/r/c/vpp/+/40361>`_ [veC 100]: vlib: remove the now unrequired frame queue check count.    - there is now an accurate measure of whether frame queues are populated.

**Nick Zavaritsky** <nick.zavaritsky@emnify.com>:

  | `39477 <https:////gerrit.fd.io/r/c/vpp/+/39477>`_ [VeC 161]: geneve: support custom options in decap

**Nikita Skrynnik** <nikita.skrynnik@xored.com>:

  | `40325 <https:////gerrit.fd.io/r/c/vpp/+/40325>`_ [Vec 68]: ping: Allow to specify a source interface in ping binary API
  | `40246 <https:////gerrit.fd.io/r/c/vpp/+/40246>`_ [VeC 76]: ping: Check only PING_RESPONSE_IP4 and PING_RESPONSE_IP6 events

**Nithinsen Kaithakadan** <nkaithakadan@marvell.com>:

  | `40548 <https:////gerrit.fd.io/r/c/vpp/+/40548>`_ [VeC 57]: octeon: add crypto framework

**Oussama Drici** <o.drici@esi-sba.dz>:

  | `40488 <https:////gerrit.fd.io/r/c/vpp/+/40488>`_ [VeC 56]: bfd: move bfd to plugin, fix checkstyle, fix bfd test, bfd docs,

**Pierre Pfister** <ppfister@cisco.com>:

  | `40758 <https:////gerrit.fd.io/r/c/vpp/+/40758>`_ [vEc 21]: build: add config option for LD_PRELOAD

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `40379 <https:////gerrit.fd.io/r/c/vpp/+/40379>`_ [VeC 95]: linux-cp: populate mapping vif-sw_if_index only for default-ns
  | `40292 <https:////gerrit.fd.io/r/c/vpp/+/40292>`_ [VeC 113]: tap: add virtio polling option

**Todd Hsiao** <tohsiao@cisco.com>:

  | `40462 <https:////gerrit.fd.io/r/c/vpp/+/40462>`_ [vEC 26]: ip: Full reassembly and fragmentation enhancement

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `40626 <https:////gerrit.fd.io/r/c/vpp/+/40626>`_ [VEc 15]: ip6-nd: simplify API to directly set options

**Vladimir Zhigulin** <vladimir.jigulin@travelping.com>:

  | `40145 <https:////gerrit.fd.io/r/c/vpp/+/40145>`_ [VeC 39]: vppinfra: collect heap stats in constant time

**Vladislav Grishenko** <themiron@mail.ru>:

  | `40415 <https:////gerrit.fd.io/r/c/vpp/+/40415>`_ [VEc 5]: ip: mark IP_ADDRESS_DUMP as mp-safe
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VeC 42]: fib: fix udp encap mp-safe ops and id validation
  | `40627 <https:////gerrit.fd.io/r/c/vpp/+/40627>`_ [VeC 47]: fib: fix invalid udp encap id cases
  | `40436 <https:////gerrit.fd.io/r/c/vpp/+/40436>`_ [Vec 49]: ip: mark IP_TABLE_DUMP and IP_ROUTE_DUMP as mp-safe
  | `40440 <https:////gerrit.fd.io/r/c/vpp/+/40440>`_ [VeC 54]: fib: add ip4 fib preallocation support
  | `35726 <https:////gerrit.fd.io/r/c/vpp/+/35726>`_ [VeC 54]: papi: fix socket api max message id calculation
  | `39579 <https:////gerrit.fd.io/r/c/vpp/+/39579>`_ [VeC 58]: fib: ensure mpls dpo index is valid for its next node
  | `40629 <https:////gerrit.fd.io/r/c/vpp/+/40629>`_ [VeC 58]: stats: add interface link speed to statseg
  | `40628 <https:////gerrit.fd.io/r/c/vpp/+/40628>`_ [VeC 58]: stats: add sw interface tags to statseg
  | `38524 <https:////gerrit.fd.io/r/c/vpp/+/38524>`_ [VeC 58]: fib: fix interface resolve from unlinked fib entries
  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [VeC 58]: mpls: fix crashes on mpls tunnel create/delete
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VeC 87]: nat: fix nat44-ed address removal from fib
  | `40413 <https:////gerrit.fd.io/r/c/vpp/+/40413>`_ [VeC 87]: nat: stick nat44-ed to use configured outside-fib

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `40666 <https:////gerrit.fd.io/r/c/vpp/+/40666>`_ [VeC 49]: ipsec: cli: 'set interface ipsec spd' support delete
  | `40377 <https:////gerrit.fd.io/r/c/vpp/+/40377>`_ [VeC 95]: vppinfra: fix cpu freq init error if cpu support aperfmperf

**jinhui li** <lijh_7@chinatelecom.cn>:

  | `40717 <https:////gerrit.fd.io/r/c/vpp/+/40717>`_ [VeC 43]: ip: discard old trace flag after copy

**kai zhang** <zhangkaiheb@126.com>:

  | `40241 <https:////gerrit.fd.io/r/c/vpp/+/40241>`_ [veC 67]: dpdk: problem in parsing max-simd-bitwidth setting

**shaohui jin** <jinshaohui789@163.com>:

  | `39776 <https:////gerrit.fd.io/r/c/vpp/+/39776>`_ [VeC 76]: vppinfra: fix memory overrun in mhash_set_mem

**sriram vatala** <svatala@marvell.com>:

  | `40615 <https:////gerrit.fd.io/r/c/vpp/+/40615>`_ [VEc 13]: octeon: add support for vnet generic flow type

**steven luong** <sluong@cisco.com>:

  | `40109 <https:////gerrit.fd.io/r/c/vpp/+/40109>`_ [VeC 110]: virtio: RSS support

Abandoned:
----------
**The following gerrit changes have not been updated in over 180 days and have been abandoned.**

**Gabriel Oginski** <gabrielx.oginski@intel.com>:

  | `39590 <https:////gerrit.fd.io/r/c/vpp/+/39590>`_ [A 180]: interface: move set rss queues function

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
authors          73
maintainers      38
committers       3
abandoned        1
================ ===

