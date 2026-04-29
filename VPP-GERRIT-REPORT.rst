
==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Wednesday 2026-04-29, 04:38:18
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

af_xdp: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `45033 <https:////gerrit.fd.io/r/c/vpp/+/45033>`_ [VECr 1]: af_xdp: add support for multi-buffer
  | `44559 <https:////gerrit.fd.io/r/c/vpp/+/44559>`_ [VECr 1]: af_xdp: reject too long host interface names
  | `45379 <https:////gerrit.fd.io/r/c/vpp/+/45379>`_ [VECr 17]: af_xdp: add mac-reuse option
  | `45501 <https:////gerrit.fd.io/r/c/vpp/+/45501>`_ [VECr 18]: af_xdp: cleanup fds and netns on error

cdp: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `44858 <https:////gerrit.fd.io/r/c/vpp/+/44858>`_ [VECr 28]: l2: fix missing CDP hello packets on BVI interface

classify: **Dave Barach** <vpp@barachs.net>
  | `42958 <https:////gerrit.fd.io/r/c/vpp/+/42958>`_ [VECr 18]: tm: add 'mark_flow' action for traffic management

cnat: **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Neale Ranns** <neale@graphiant.com>
  | `43369 <https:////gerrit.fd.io/r/c/vpp/+/43369>`_ [VECr 0]: cnat: support encapsulation and session cleanup on backend deletion

crypto: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>
  | `45654 <https:////gerrit.fd.io/r/c/vpp/+/45654>`_ [VECr 0]: crypto: add vnet_crypto_ctx_create_max
  | `45205 <https:////gerrit.fd.io/r/c/vpp/+/45205>`_ [VECr 4]: crypto: add aad28, aad20 gcm variants
  | `45510 <https:////gerrit.fd.io/r/c/vpp/+/45510>`_ [VECr 15]: crypto: add op tracing capability

ct6: **Dave Barach** <vpp@barachs.net>
  | `45410 <https:////gerrit.fd.io/r/c/vpp/+/45410>`_ [VECr 25]: ct6: fix multi-worker session lookup and allow non-physical interfaces
  | `45411 <https:////gerrit.fd.io/r/c/vpp/+/45411>`_ [VECr 25]: ct6: move ct6-in2out from interface-output to ip6-unicast arc

dev: **Damjan Marion** <damarion@cisco.com>
  | `45590 <https:////gerrit.fd.io/r/c/vpp/+/45590>`_ [VECr 0]: iavf: add L4 checksum offload on RX
  | `45246 <https:////gerrit.fd.io/r/c/vpp/+/45246>`_ [VECr 7]: flow: single-interface-per-flow model

dhcp: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `45627 <https:////gerrit.fd.io/r/c/vpp/+/45627>`_ [VECr 0]: pppoeclient: add PPPoE client plugin with DHCPv6 runtime observability

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `45573 <https:////gerrit.fd.io/r/c/vpp/+/45573>`_ [VECr 0]: docs: clarify security scope and add SECURITY.md
  | `45627 <https:////gerrit.fd.io/r/c/vpp/+/45627>`_ [VECr 0]: pppoeclient: add PPPoE client plugin with DHCPv6 runtime observability
  | `45505 <https:////gerrit.fd.io/r/c/vpp/+/45505>`_ [VECr 0]: rdma: add mlx5 TSO support for raw packet tx
  | `44450 <https:////gerrit.fd.io/r/c/vpp/+/44450>`_ [VECr 1]: misc: patch to test CI infra

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `45627 <https:////gerrit.fd.io/r/c/vpp/+/45627>`_ [VECr 0]: pppoeclient: add PPPoE client plugin with DHCPv6 runtime observability
  | `45561 <https:////gerrit.fd.io/r/c/vpp/+/45561>`_ [VECr 6]: dpdk: add 'dpdk trace save' CLI command
  | `45562 <https:////gerrit.fd.io/r/c/vpp/+/45562>`_ [VECr 6]: dpdk: add trace-bufsz startup.conf option
  | `45246 <https:////gerrit.fd.io/r/c/vpp/+/45246>`_ [VECr 7]: flow: single-interface-per-flow model

ethernet: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `44858 <https:////gerrit.fd.io/r/c/vpp/+/44858>`_ [VECr 28]: l2: fix missing CDP hello packets on BVI interface

fib: **Neale Ranns** <neale@graphiant.com>
  | `43892 <https:////gerrit.fd.io/r/c/vpp/+/43892>`_ [VECr 1]: fib: compute fib entry flags from full path list

flow: **Damjan Marion** <damarion@cisco.com>
  | `45246 <https:////gerrit.fd.io/r/c/vpp/+/45246>`_ [VECr 7]: flow: single-interface-per-flow model

gtpu: **Hongjun Ni** <hongjun.ni@intel.com>
  | `45246 <https:////gerrit.fd.io/r/c/vpp/+/45246>`_ [VECr 7]: flow: single-interface-per-flow model

hs-test: **Florin Coras** <fcoras@cisco.com>, **Matus Fabian** <matfabia@cisco.com>
  | `45581 <https:////gerrit.fd.io/r/c/vpp/+/45581>`_ [VECr 0]: tcp: hs-test test harness

hsa: **Florin Coras** <fcoras@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>
  | `45581 <https:////gerrit.fd.io/r/c/vpp/+/45581>`_ [VECr 0]: tcp: hs-test test harness

http: **Florin Coras** <fcoras@cisco.com>
  | `45658 <https:////gerrit.fd.io/r/c/vpp/+/45658>`_ [VECr 0]: http: http2_update_time_callback improvement

iavf: **Damjan Marion** <damarion@cisco.com>
  | `45590 <https:////gerrit.fd.io/r/c/vpp/+/45590>`_ [VECr 0]: iavf: add L4 checksum offload on RX
  | `45159 <https:////gerrit.fd.io/r/c/vpp/+/45159>`_ [VECr 0]: iavf: fix native TSO datapath for 1500-byte frames
  | `45452 <https:////gerrit.fd.io/r/c/vpp/+/45452>`_ [VECr 1]: iavf: fix REQUEST_QUEUES timeout and irq guards

interface: **Dave Barach** <vpp@barachs.net>
  | `45246 <https:////gerrit.fd.io/r/c/vpp/+/45246>`_ [VECr 7]: flow: single-interface-per-flow model
  | `45536 <https:////gerrit.fd.io/r/c/vpp/+/45536>`_ [VECr 11]: interface: enable IPv6 link state on unnumbered interfaces

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `45472 <https:////gerrit.fd.io/r/c/vpp/+/45472>`_ [VECr 6]: ip: add multicast SVR
  | `45478 <https:////gerrit.fd.io/r/c/vpp/+/45478>`_ [VECr 6]: ip: svr add bit indicating fragmentation to vnet_buffer
  | `45494 <https:////gerrit.fd.io/r/c/vpp/+/45494>`_ [VECr 6]: ip: fix reassembly bugs and add tests
  | `45495 <https:////gerrit.fd.io/r/c/vpp/+/45495>`_ [VECr 6]: ip: fix reassembly bugs, add extended SV reass CLI and tests
  | `45504 <https:////gerrit.fd.io/r/c/vpp/+/45504>`_ [VECr 16]: ip6-nd: support RDNSS option in IPv6 RA
  | `42958 <https:////gerrit.fd.io/r/c/vpp/+/42958>`_ [VECr 18]: tm: add 'mark_flow' action for traffic management
  | `44948 <https:////gerrit.fd.io/r/c/vpp/+/44948>`_ [VECr 28]: ip6: fix show ip6-ll cli if selector

ip6-nd: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `45503 <https:////gerrit.fd.io/r/c/vpp/+/45503>`_ [VECr 15]: ip6-nd: update secondary RA prefixes for subnets
  | `45504 <https:////gerrit.fd.io/r/c/vpp/+/45504>`_ [VECr 16]: ip6-nd: support RDNSS option in IPv6 RA
  | `45046 <https:////gerrit.fd.io/r/c/vpp/+/45046>`_ [VECr 20]: ip6-nd: add punt reason for neigh advs
  | `45099 <https:////gerrit.fd.io/r/c/vpp/+/45099>`_ [VECr 20]: ip6-nd: add nd-proxy all dst

ipsec: **Neale Ranns** <neale@graphiant.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `45510 <https:////gerrit.fd.io/r/c/vpp/+/45510>`_ [VECr 15]: crypto: add op tracing capability

l2: **John Lo** <lojultra2020@outlook.com>, **Steven Luong** <sluong@cisco.com>
  | `44858 <https:////gerrit.fd.io/r/c/vpp/+/44858>`_ [VECr 28]: l2: fix missing CDP hello packets on BVI interface

lb: **Pfister** <ppfister@cisco.com>, **Hongjun Ni** <hongjun.ni@intel.com>
  | `45487 <https:////gerrit.fd.io/r/c/vpp/+/45487>`_ [VECr 13]: lb: Allow setting weight on AS
  | `45428 <https:////gerrit.fd.io/r/c/vpp/+/45428>`_ [VECr 14]: lb: API bugfix
  | `45431 <https:////gerrit.fd.io/r/c/vpp/+/45431>`_ [VECr 20]: lb: Add punt feature to per-port VIPs

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `45627 <https:////gerrit.fd.io/r/c/vpp/+/45627>`_ [VECr 0]: pppoeclient: add PPPoE client plugin with DHCPv6 runtime observability

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `45573 <https:////gerrit.fd.io/r/c/vpp/+/45573>`_ [VECr 0]: docs: clarify security scope and add SECURITY.md
  | `45627 <https:////gerrit.fd.io/r/c/vpp/+/45627>`_ [VECr 0]: pppoeclient: add PPPoE client plugin with DHCPv6 runtime observability
  | `43369 <https:////gerrit.fd.io/r/c/vpp/+/43369>`_ [VECr 0]: cnat: support encapsulation and session cleanup on backend deletion
  | `45644 <https:////gerrit.fd.io/r/c/vpp/+/45644>`_ [VECr 1]: misc: update vpp_if_stats govpp version
  | `45205 <https:////gerrit.fd.io/r/c/vpp/+/45205>`_ [VECr 4]: crypto: add aad28, aad20 gcm variants
  | `45478 <https:////gerrit.fd.io/r/c/vpp/+/45478>`_ [VECr 6]: ip: svr add bit indicating fragmentation to vnet_buffer
  | `45510 <https:////gerrit.fd.io/r/c/vpp/+/45510>`_ [VECr 15]: crypto: add op tracing capability
  | `45374 <https:////gerrit.fd.io/r/c/vpp/+/45374>`_ [VECr 29]: build rpm-packaging: make vpp rpm package for kylinV11

octeon: **Monendra Singh Kushwaha** <kmonendra@marvell.com>, **Damjan Marion** <damarion@cisco.com>
  | `45246 <https:////gerrit.fd.io/r/c/vpp/+/45246>`_ [VECr 7]: flow: single-interface-per-flow model

ping: **Andrew Yourtchenko** <ayourtch@gmail.com>
  | `45502 <https:////gerrit.fd.io/r/c/vpp/+/45502>`_ [VECr 17]: ping: set LOCALLY_ORIGINATED flag on cli-initiated ping packets.

quic: **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Florin Coras** <fcoras@cisco.com>
  | `45655 <https:////gerrit.fd.io/r/c/vpp/+/45655>`_ [VECr 0]: quic: fix the use of vpp crypto engines in quic

rdma: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `45627 <https:////gerrit.fd.io/r/c/vpp/+/45627>`_ [VECr 0]: pppoeclient: add PPPoE client plugin with DHCPv6 runtime observability
  | `45505 <https:////gerrit.fd.io/r/c/vpp/+/45505>`_ [VECr 0]: rdma: add mlx5 TSO support for raw packet tx
  | `45582 <https:////gerrit.fd.io/r/c/vpp/+/45582>`_ [VECr 1]: rdma: RX L4 checksum offload for mlx5dv devices

sfdp: **Mohammed Hawari** <mohammed@hawari.fr>, **Hadi Rayan Al-Sandid** <halsandi@cisco.com>, **Guillaume Solignac** <gsoligna@cisco.com>, **Ole Troan** <otroan@employees.org>
  | `45101 <https:////gerrit.fd.io/r/c/vpp/+/45101>`_ [VECr 0]: sfdp: guard packet bit shifts in lookup

snort: **Damjan Marion** <damarion@cisco.com>
  | `45597 <https:////gerrit.fd.io/r/c/vpp/+/45597>`_ [VECr 0]: snort: include string.h in daq source files
  | `44923 <https:////gerrit.fd.io/r/c/vpp/+/44923>`_ [VECr 21]: snort: copy metadata from original to generated packets

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `45627 <https:////gerrit.fd.io/r/c/vpp/+/45627>`_ [VECr 0]: pppoeclient: add PPPoE client plugin with DHCPv6 runtime observability
  | `44572 <https:////gerrit.fd.io/r/c/vpp/+/44572>`_ [VECr 0]: virtio: add native plugin L2 xconnect test with QEMU
  | `43369 <https:////gerrit.fd.io/r/c/vpp/+/43369>`_ [VECr 0]: cnat: support encapsulation and session cleanup on backend deletion
  | `45101 <https:////gerrit.fd.io/r/c/vpp/+/45101>`_ [VECr 0]: sfdp: guard packet bit shifts in lookup
  | `45651 <https:////gerrit.fd.io/r/c/vpp/+/45651>`_ [VECr 0]: sfdp: add tests helper class
  | `45033 <https:////gerrit.fd.io/r/c/vpp/+/45033>`_ [VECr 1]: af_xdp: add support for multi-buffer
  | `45600 <https:////gerrit.fd.io/r/c/vpp/+/45600>`_ [VECr 1]: crypto: fix ctx engine key data leak on re-key
  | `45494 <https:////gerrit.fd.io/r/c/vpp/+/45494>`_ [VECr 6]: ip: fix reassembly bugs and add tests
  | `45495 <https:////gerrit.fd.io/r/c/vpp/+/45495>`_ [VECr 6]: ip: fix reassembly bugs, add extended SV reass CLI and tests
  | `45420 <https:////gerrit.fd.io/r/c/vpp/+/45420>`_ [VECr 6]: tests: replace set_errors_str with "show error" CLI
  | `45487 <https:////gerrit.fd.io/r/c/vpp/+/45487>`_ [VECr 13]: lb: Allow setting weight on AS
  | `45428 <https:////gerrit.fd.io/r/c/vpp/+/45428>`_ [VECr 14]: lb: API bugfix
  | `45504 <https:////gerrit.fd.io/r/c/vpp/+/45504>`_ [VECr 16]: ip6-nd: support RDNSS option in IPv6 RA
  | `45046 <https:////gerrit.fd.io/r/c/vpp/+/45046>`_ [VECr 20]: ip6-nd: add punt reason for neigh advs
  | `45099 <https:////gerrit.fd.io/r/c/vpp/+/45099>`_ [VECr 20]: ip6-nd: add nd-proxy all dst
  | `45431 <https:////gerrit.fd.io/r/c/vpp/+/45431>`_ [VECr 20]: lb: Add punt feature to per-port VIPs

unittest: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `45600 <https:////gerrit.fd.io/r/c/vpp/+/45600>`_ [VECr 1]: crypto: fix ctx engine key data leak on re-key
  | `43892 <https:////gerrit.fd.io/r/c/vpp/+/43892>`_ [VECr 1]: fib: compute fib entry flags from full path list
  | `45205 <https:////gerrit.fd.io/r/c/vpp/+/45205>`_ [VECr 4]: crypto: add aad28, aad20 gcm variants

vcl: **Florin Coras** <fcoras@cisco.com>
  | `44450 <https:////gerrit.fd.io/r/c/vpp/+/44450>`_ [VECr 1]: misc: patch to test CI infra

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `45469 <https:////gerrit.fd.io/r/c/vpp/+/45469>`_ [VECr 6]: vlib: avoid warning by using correct node fn declaration
  | `45583 <https:////gerrit.fd.io/r/c/vpp/+/45583>`_ [VECr 7]: vlib: fix trace flag loss when multiple pending frames share next frame
  | `43538 <https:////gerrit.fd.io/r/c/vpp/+/43538>`_ [VECr 28]: stats: show raw value in show stat segment

vpp: **Dave Barach** <vpp@barachs.net>
  | `45627 <https:////gerrit.fd.io/r/c/vpp/+/45627>`_ [VECr 0]: pppoeclient: add PPPoE client plugin with DHCPv6 runtime observability

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `44519 <https:////gerrit.fd.io/r/c/vpp/+/44519>`_ [VECr 0]: vppinfra: format_hexdump_trunc, unformat_base10, format_backtrace
  | `45470 <https:////gerrit.fd.io/r/c/vpp/+/45470>`_ [VECr 6]: vppinfra: add cast to prevent warning
  | `45471 <https:////gerrit.fd.io/r/c/vpp/+/45471>`_ [VECr 6]: vppinfra: add const-qualifier to avoid warning(s)

vxlan: **John Lo** <lojultra2020@outlook.com>, **Steven Luong** <sluong@cisco.com>
  | `45246 <https:////gerrit.fd.io/r/c/vpp/+/45246>`_ [VECr 7]: flow: single-interface-per-flow model

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Akos Orban** <orbanakos2001@gmail.com>:

  | `45001 <https:////gerrit.fd.io/r/c/vpp/+/45001>`_ [VeC 63]: cnat: fix show cnat translation for specific translation id
  | `44995 <https:////gerrit.fd.io/r/c/vpp/+/44995>`_ [VeC 63]: cnat: fix show cnat client showing invalid for client id

**Alexander Chernavin** <chernavin@mts.ru>:

  | `43726 <https:////gerrit.fd.io/r/c/vpp/+/43726>`_ [vEc 28]: vhost: fix rxvq interrupts triggered because of race

**Alok Mishra** <almishra@marvell.com>:

  | `42257 <https:////gerrit.fd.io/r/c/vpp/+/42257>`_ [VeC 50]: octeon: implement hardware traffic management

**Andrew Mason** <mason12@gmail.com>:

  | `44082 <https:////gerrit.fd.io/r/c/vpp/+/44082>`_ [vec 173]: linux-cp: Punt for ISIS traffic over linux-cp plugin
  | `44085 <https:////gerrit.fd.io/r/c/vpp/+/44085>`_ [veC 173]: linux-cp: Punt for ISIS traffic over linux-cp plugin

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `41210 <https:////gerrit.fd.io/r/c/vpp/+/41210>`_ [veC 97]: build: disable the "new" way of handling API dependencies which relies on a broken CMake feature

**Anna Neiman** <anna.neiman@insidepacket.com>:

  | `43046 <https:////gerrit.fd.io/r/c/vpp/+/43046>`_ [VeC 125]: feature: Call dvr_dpo_unlock in case delete SW interface - in order enable feature ip4-dvr-reinject on the following addition interface ;add arch index in show features

**Aritra Basu** <aritrbas@cisco.com>:

  | `45012 <https:////gerrit.fd.io/r/c/vpp/+/45012>`_ [VeC 39]: ip-neighbor: suppress off-link adj-fib on addressed interfaces
  | `45268 <https:////gerrit.fd.io/r/c/vpp/+/45268>`_ [VeC 41]: ip6-nd: enforce on-link source validation for RS neighbor learning
  | `45073 <https:////gerrit.fd.io/r/c/vpp/+/45073>`_ [VeC 41]: fib: honor unnumbered RX interface in MFIB RPF check
  | `45074 <https:////gerrit.fd.io/r/c/vpp/+/45074>`_ [VeC 41]: ip6-nd: enforce on-link source validation for ND learning
  | `45260 <https:////gerrit.fd.io/r/c/vpp/+/45260>`_ [VeC 41]: ip6-nd: add per-interface control for inbound RA acceptance
  | `44350 <https:////gerrit.fd.io/r/c/vpp/+/44350>`_ [VeC 47]: ip6-nd: fix unicast NA handling in ND proxy

**Bartlomiej Leszak** <bartlomiej.leszak@gmail.com>:

  | `42978 <https:////gerrit.fd.io/r/c/vpp/+/42978>`_ [VeC 125]: pnat: do not disable pnat on rule deletion

**Benoît Ganne** <bganne@cisco.com>:

  | `45601 <https:////gerrit.fd.io/r/c/vpp/+/45601>`_ [VEc 1]: vlib: fix one-time barrier release callbacks
  | `39443 <https:////gerrit.fd.io/r/c/vpp/+/39443>`_ [vEC 1]: vnet: reorder vnet_buffer2 metadata
  | `45203 <https:////gerrit.fd.io/r/c/vpp/+/45203>`_ [VeC 47]: policer: avoid redundant l2_overhead array access on TX path
  | `44962 <https:////gerrit.fd.io/r/c/vpp/+/44962>`_ [VeC 69]: pppoe: initialize sw_if_index before early goto

**Damjan Marion** <dmarion@0xa5.net>:

  | `45409 <https:////gerrit.fd.io/r/c/vpp/+/45409>`_ [vEC 25]: ikev2: add Curve25519 and Curve448 DH groups
  | `44092 <https:////gerrit.fd.io/r/c/vpp/+/44092>`_ [veC 167]: ipsec: precompute payload and payload length adjustments
  | `44081 <https:////gerrit.fd.io/r/c/vpp/+/44081>`_ [veC 172]: ipsec: fill op templates with lengths and tag sizes

**Duncan Eastoe** <duncaneastoe+github@gmail.com>:

  | `45042 <https:////gerrit.fd.io/r/c/vpp/+/45042>`_ [VeC 41]: stats: stat_segment_ls_r() only return NULL on error
  | `45043 <https:////gerrit.fd.io/r/c/vpp/+/45043>`_ [VeC 41]: stats: don't leak regcomp() allocated memory

**FDio GitHub Actions** <releng+fdio-github@linuxfoundation.org>:

  | `45227 <https:////gerrit.fd.io/r/c/vpp/+/45227>`_ [veC 43]: build(deps): bump step-security/harden-runner from 2.13.2 to 2.16.0
  | `45225 <https:////gerrit.fd.io/r/c/vpp/+/45225>`_ [veC 43]: build(deps): bump lfreleng-actions/github2gerrit-action from 1.0.5 to 1.0.8

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `45564 <https:////gerrit.fd.io/r/c/vpp/+/45564>`_ [VEc 0]: sfdp: add api enum for timeouts
  | `44754 <https:////gerrit.fd.io/r/c/vpp/+/44754>`_ [VEc 25]: tracepath: introduce tracepath plugin
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VeC 32]: sfdp: add sfdp-session-stats service
  | `44847 <https:////gerrit.fd.io/r/c/vpp/+/44847>`_ [Vec 64]: sfdp: modify tenant_index type from u16 to u32
  | `44474 <https:////gerrit.fd.io/r/c/vpp/+/44474>`_ [Vec 111]: sasc: fix tenant_index overlap in sasc_buffer

**Ivan Ivanets** <iivanets@cisco.com>:

  | `45656 <https:////gerrit.fd.io/r/c/vpp/+/45656>`_ [vEC 0]: tests: add quic vpp crypto
  | `42150 <https:////gerrit.fd.io/r/c/vpp/+/42150>`_ [VeC 33]: tests: reduce sleep interval in ip-neighbor age test
  | `44827 <https:////gerrit.fd.io/r/c/vpp/+/44827>`_ [VeC 62]: crypto: unify per-thread key_data allocation

**Jerome Labidurie** <jerome.labidurie@orange.com>:

  | `44849 <https:////gerrit.fd.io/r/c/vpp/+/44849>`_ [VeC 81]: policer: api to unaply policer from any interface
  | `44844 <https:////gerrit.fd.io/r/c/vpp/+/44844>`_ [VeC 81]: policer: prevent policer to be applied twice
  | `44843 <https:////gerrit.fd.io/r/c/vpp/+/44843>`_ [VeC 81]: policer: fix crash when unapplying a policer
  | `44693 <https:////gerrit.fd.io/r/c/vpp/+/44693>`_ [VeC 81]: policer: obtain policers applied to an interface

**Jing Peng** <jing@meter.com>:

  | `37058 <https:////gerrit.fd.io/r/c/vpp/+/37058>`_ [VeC 83]: vppapigen: fix json build error

**Maxime Peim** <maxime.peim@gmail.com>:

  | `45296 <https:////gerrit.fd.io/r/c/vpp/+/45296>`_ [VeC 36]: ethernet: implement outer_vlan_id_any sub-interface matching
  | `45280 <https:////gerrit.fd.io/r/c/vpp/+/45280>`_ [VeC 36]: gso: implement IPv6 extension header traversal
  | `45249 <https:////gerrit.fd.io/r/c/vpp/+/45249>`_ [VeC 42]: policer: fix DSCP marking for VLAN-tagged packets
  | `45252 <https:////gerrit.fd.io/r/c/vpp/+/45252>`_ [VeC 42]: policer: fix unchecked policer removal
  | `45253 <https:////gerrit.fd.io/r/c/vpp/+/45253>`_ [veC 42]: policer: reject delete of policer still applied to interface
  | `45254 <https:////gerrit.fd.io/r/c/vpp/+/45254>`_ [VeC 42]: policer: reject deletion of policer used by punt policing

**Mohammad Mahdi Nemati Haravani** <nemati.mahdi255@gmail.com>:

  | `44303 <https:////gerrit.fd.io/r/c/vpp/+/44303>`_ [vEC 17]: build: fix etc path for vpp-ext-deps package fix the bug vpp ext deb for DPDK 25.07 and MLX5 PMD topic

**Mohammed HAWARI** <momohawari@gmail.com>:

  | `42343 <https:////gerrit.fd.io/r/c/vpp/+/42343>`_ [VeC 139]: vcl: LDP default to regular option

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `44919 <https:////gerrit.fd.io/r/c/vpp/+/44919>`_ [VeC 41]: snort: fix inject/finalize ordering race in deq node
  | `45177 <https:////gerrit.fd.io/r/c/vpp/+/45177>`_ [VeC 47]: sfdp: add blacklist/whitelist to snort service
  | `42886 <https:////gerrit.fd.io/r/c/vpp/+/42886>`_ [VeC 70]: ipip: fix support for ipip6o6 from linux tunnel
  | `44715 <https:////gerrit.fd.io/r/c/vpp/+/44715>`_ [Vec 74]: pg: Guard against non‑monotonic time and negative accumulator
  | `44426 <https:////gerrit.fd.io/r/c/vpp/+/44426>`_ [VeC 109]: virtio: add the check if MAC feature is negotiated

**Moinak Bhattacharyya** <moinakb001@gmail.com>:

  | `44708 <https:////gerrit.fd.io/r/c/vpp/+/44708>`_ [VeC 87]: iouring: Add io_uring plugin to allow polling usage of io_uring

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `44903 <https:////gerrit.fd.io/r/c/vpp/+/44903>`_ [VeC 64]: vxlan: reset next_dpo on delete
  | `44961 <https:////gerrit.fd.io/r/c/vpp/+/44961>`_ [Vec 69]: ip6-nd: support RA pfx info option with flag L&!A

**Nicolas PLANEL** <nplanel@gmail.com>:

  | `45642 <https:////gerrit.fd.io/r/c/vpp/+/45642>`_ [VEc 1]: dpdk: enable MBUF_FAST_FREE TX offload when multi-seg is disabled
  | `44976 <https:////gerrit.fd.io/r/c/vpp/+/44976>`_ [vEc 7]: sfdp: async offload lookup

**Ole Troan** <otroan@employees.org>:

  | `45649 <https:////gerrit.fd.io/r/c/vpp/+/45649>`_ [vEC 0]: vppapigen: union endian generation
  | `45496 <https:////gerrit.fd.io/r/c/vpp/+/45496>`_ [VEc 13]: papi: improve performance on set_errors

**Parth Sahu** <parthsahu15@gmail.com>:

  | `44813 <https:////gerrit.fd.io/r/c/vpp/+/44813>`_ [VeC 88]: session auto_sdl: fix SDL show rule argument order
  | `44796 <https:////gerrit.fd.io/r/c/vpp/+/44796>`_ [veC 90]: fix: correct fixstyle in session_sdl command function

**Robert Shearman** <robertshearman@gmail.com>:

  | `44551 <https:////gerrit.fd.io/r/c/vpp/+/44551>`_ [VeC 40]: vppapigen: fix inconsistency in paths JSON

**Ryosuke Nakayama** <ryosuke_666@icloud.com>:

  | `45604 <https:////gerrit.fd.io/r/c/vpp/+/45604>`_ [VEc 0]: cnat: make snat policy del paths re-entrant

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `44230 <https:////gerrit.fd.io/r/c/vpp/+/44230>`_ [vEC 28]: linux-cp: bind lcp_router_table lifetime to lcp_itf_pair
  | `44232 <https:////gerrit.fd.io/r/c/vpp/+/44232>`_ [VeC 123]: linux-cp: fix cleanup of special routes
  | `44241 <https:////gerrit.fd.io/r/c/vpp/+/44241>`_ [Vec 131]: linux-cp: on remove do cleanup for all fibs
  | `44249 <https:////gerrit.fd.io/r/c/vpp/+/44249>`_ [VeC 146]: fib: dump by src not only contributing routes

**Venkata Ravichandra Mynidi** <vmynidi@marvell.com>:

  | `40775 <https:////gerrit.fd.io/r/c/vpp/+/40775>`_ [Vec 34]: tm: add tm framework for hw traffic management

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `45650 <https:////gerrit.fd.io/r/c/vpp/+/45650>`_ [VEc 0]: flowprobe: count based sampling support

**Vladimir Zhigulin** <vladimir.jigulin@travelping.com>:

  | `40145 <https:////gerrit.fd.io/r/c/vpp/+/40145>`_ [vEC 28]: vppinfra: collect heap stats in constant time

**Vladislav Grishenko** <themiron@mail.ru>:

  | `44575 <https:////gerrit.fd.io/r/c/vpp/+/44575>`_ [VeC 109]: fib: add interface-rx dpo mpls support
  | `44574 <https:////gerrit.fd.io/r/c/vpp/+/44574>`_ [VeC 109]: fib: fix stale interface-rx dpo fib after deag/lookup
  | `41660 <https:////gerrit.fd.io/r/c/vpp/+/41660>`_ [VeC 109]: nat: add nat44-ed ipfix dst address and port logging
  | `42538 <https:////gerrit.fd.io/r/c/vpp/+/42538>`_ [VeC 109]: nat: speedup nat44-ed vrf table lookups
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VeC 109]: nat: fix nat44-ed address removal from fib
  | `44563 <https:////gerrit.fd.io/r/c/vpp/+/44563>`_ [veC 110]: ip: fix DSCP CS7 value
  | `44568 <https:////gerrit.fd.io/r/c/vpp/+/44568>`_ [VeC 110]: vxlan: add default dscp value config for vxlan encap
  | `44567 <https:////gerrit.fd.io/r/c/vpp/+/44567>`_ [VeC 110]: udp: add default dscp value config for udp encap
  | `40627 <https:////gerrit.fd.io/r/c/vpp/+/40627>`_ [VeC 110]: fib: fix invalid udp encap id cases
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VeC 110]: fib: fix udp encap mp-safe ops and id validation
  | `43180 <https:////gerrit.fd.io/r/c/vpp/+/43180>`_ [VeC 110]: fib: avoid loadbalance dpo node path polarisation
  | `40630 <https:////gerrit.fd.io/r/c/vpp/+/40630>`_ [VeC 110]: vlib: mark cli quit command as mp_safe

**Vratko Polak** <vrpolak@cisco.com>:

  | `45528 <https:////gerrit.fd.io/r/c/vpp/+/45528>`_ [vEC 13]: empty change for GHA(CSIT) testing

**Xiangqing Cheng** <chengxq@chinatelecom.cn>:

  | `42849 <https:////gerrit.fd.io/r/c/vpp/+/42849>`_ [VeC 125]: ip-neighbor: ARP/NA per-interface counter improvements

**echo** <614699596@qq.com>:

  | `45348 <https:////gerrit.fd.io/r/c/vpp/+/45348>`_ [VeC 32]: bpf_trace_filter: fix bpf_expr memory leak on error path

**joydeep ghosh** <joydeep779@gmail.com>:

  | `44631 <https:////gerrit.fd.io/r/c/vpp/+/44631>`_ [vec 77]: dns: fix crash when no usable source address exists

**lei feng** <1579628578@qq.com>:

  | `42077 <https:////gerrit.fd.io/r/c/vpp/+/42077>`_ [VEc 28]: dns: dns request ip6 fix
  | `42129 <https:////gerrit.fd.io/r/c/vpp/+/42129>`_ [VEc 28]: dns: support ipv6 server to resolve name
  | `42064 <https:////gerrit.fd.io/r/c/vpp/+/42064>`_ [vec 82]: docs: Python apis examples

**niklesh** <nikleshparshaboina@gmail.com>:

  | `45016 <https:////gerrit.fd.io/r/c/vpp/+/45016>`_ [VEc 0]: cnat: add scope_id to session key

**nleblanc** <nleblanc@joustsec.com>:

  | `45271 <https:////gerrit.fd.io/r/c/vpp/+/45271>`_ [VeC 40]: linux-cp: prevent MAC address sync on non-Ethernet interfaces on RTM_NEWLINK

**pkt4u** <pkt4u@outlook.com>:

  | `44208 <https:////gerrit.fd.io/r/c/vpp/+/44208>`_ [vEC 28]: lb: fix API byte order and IPv4 prefix length handling
  | `44207 <https:////gerrit.fd.io/r/c/vpp/+/44207>`_ [VeC 122]: lb: fix incorrect byte order conversion for vip port display

**ruici wang** <964491902@qq.com>:

  | `44100 <https:////gerrit.fd.io/r/c/vpp/+/44100>`_ [veC 167]: ipsec: prevent use of deleted keys in async mode

**shaohui jin** <jinshaohui789@163.com>:

  | `44928 <https:////gerrit.fd.io/r/c/vpp/+/44928>`_ [veC 55]: fib: IPv4 Route Query Command Crash

**steven luong** <sluong@cisco.com>:

  | `44420 <https:////gerrit.fd.io/r/c/vpp/+/44420>`_ [VEc 1]: session: make transport to use application's segment manager
  | `44569 <https:////gerrit.fd.io/r/c/vpp/+/44569>`_ [VeC 110]: vppinfra: clib_time_verify_frequency may cause time jump

**yelena_c@rad.com** <yelena_c@rad.com>:

  | `44536 <https:////gerrit.fd.io/r/c/vpp/+/44536>`_ [veC 92]: hs-test: fix CI infra issues
  | `44421 <https:////gerrit.fd.io/r/c/vpp/+/44421>`_ [VeC 92]: l2: fix null pointer access in l2-efp-filter

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
maintainers      56
committers       0
abandoned        0
================ ===

