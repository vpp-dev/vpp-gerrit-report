
==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Wednesday 2026-04-01, 04:19:28
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
  | `45033 <https:////gerrit.fd.io/r/c/vpp/+/45033>`_ [VECr 0]: af_xdp: add support for multi-buffer

bpf_trace_filter: **Mohammed Hawari** <mohammed@hawari.fr>
  | `45348 <https:////gerrit.fd.io/r/c/vpp/+/45348>`_ [VECr 4]: bpf_trace_filter: fix bpf_expr memory leak on error path

bufmon: **Benoît Ganne** <bganne@cisco.com>
  | `45110 <https:////gerrit.fd.io/r/c/vpp/+/45110>`_ [VECr 4]: bufmon: unregister old callbacks before re-registering on enable

build: **Damjan Marion** <damarion@cisco.com>
  | `45033 <https:////gerrit.fd.io/r/c/vpp/+/45033>`_ [VECr 0]: af_xdp: add support for multi-buffer
  | `45119 <https:////gerrit.fd.io/r/c/vpp/+/45119>`_ [VECr 25]: build: add Fedora 43 build compatibility
  | `45112 <https:////gerrit.fd.io/r/c/vpp/+/45112>`_ [VECr 25]: build: add AlmaLinux support to install-dep target

cdp: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `44858 <https:////gerrit.fd.io/r/c/vpp/+/44858>`_ [VECr 0]: l2: fix missing CDP hello packets on BVI interface

classify: **Dave Barach** <vpp@barachs.net>
  | `42958 <https:////gerrit.fd.io/r/c/vpp/+/42958>`_ [VECr 22]: tm: add 'mark_flow' action for traffic management

cnat: **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Neale Ranns** <neale@graphiant.com>
  | `43369 <https:////gerrit.fd.io/r/c/vpp/+/43369>`_ [VECr 1]: cnat: support encapsulation and session cleanup on backend deletion

dhcp: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `45358 <https:////gerrit.fd.io/r/c/vpp/+/45358>`_ [VECr 1]: dhcp: export DHCPv6 runtime state for PPPoE observability

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `44450 <https:////gerrit.fd.io/r/c/vpp/+/44450>`_ [VECr 0]: misc: patch to test CI infra
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 4]: sfdp: add sfdp-session-stats service

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `45152 <https:////gerrit.fd.io/r/c/vpp/+/45152>`_ [VECr 1]: dpdk: install default jump-to-group-1 rule for mlx5
  | `44974 <https:////gerrit.fd.io/r/c/vpp/+/44974>`_ [VECr 1]: dpdk: enable flow offload for mlx5 driver
  | `45373 <https:////gerrit.fd.io/r/c/vpp/+/45373>`_ [VECr 1]: dpdk: add representor device flag
  | `45372 <https:////gerrit.fd.io/r/c/vpp/+/45372>`_ [VECr 1]: dpdk: remove device setup calls from flow operations
  | `45114 <https:////gerrit.fd.io/r/c/vpp/+/45114>`_ [VECr 25]: dpdk: fix maybe-uninitialized warning with GCC 15

ethernet: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `44858 <https:////gerrit.fd.io/r/c/vpp/+/44858>`_ [VECr 0]: l2: fix missing CDP hello packets on BVI interface
  | `45296 <https:////gerrit.fd.io/r/c/vpp/+/45296>`_ [VECr 8]: ethernet: implement outer_vlan_id_any sub-interface matching

fib: **Neale Ranns** <neale@graphiant.com>
  | `45073 <https:////gerrit.fd.io/r/c/vpp/+/45073>`_ [VECr 13]: fib: honor unnumbered RX interface in MFIB RPF check

flow: **Damjan Marion** <damarion@cisco.com>
  | `45063 <https:////gerrit.fd.io/r/c/vpp/+/45063>`_ [VECr 12]: flow: fix flow_ops_function check

flowprobe: **Ole Troan** <otroan@employees.org>
  | `45058 <https:////gerrit.fd.io/r/c/vpp/+/45058>`_ [VECr 20]: flowprobe: count based sampling support

gso: **Andrew Yourtchenko** <ayourtch@gmail.com>, **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>
  | `45280 <https:////gerrit.fd.io/r/c/vpp/+/45280>`_ [VECr 8]: gso: implement IPv6 extension header traversal

http: **Florin Coras** <fcoras@cisco.com>
  | `45357 <https:////gerrit.fd.io/r/c/vpp/+/45357>`_ [VECr 0]: http: optimize http_ctx_t and http_req_t size
  | `45351 <https:////gerrit.fd.io/r/c/vpp/+/45351>`_ [VECr 0]: http: http_req_t refactoring
  | `45342 <https:////gerrit.fd.io/r/c/vpp/+/45342>`_ [VECr 0]: http: move h2 and h3 aux conn ctx to http_ctx_t

iavf: **Damjan Marion** <damarion@cisco.com>
  | `45159 <https:////gerrit.fd.io/r/c/vpp/+/45159>`_ [VECr 0]: iavf: fix native AVF TSO queue setup

ikev2: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Benoît Ganne** <bganne@cisco.com>
  | `45364 <https:////gerrit.fd.io/r/c/vpp/+/45364>`_ [VECr 0]: ikev2: add AES-CTR child SA support
  | `45367 <https:////gerrit.fd.io/r/c/vpp/+/45367>`_ [VECr 0]: ikev2: add AES-CMAC integrity support
  | `45363 <https:////gerrit.fd.io/r/c/vpp/+/45363>`_ [VECr 0]: ikev2: add null encryption support
  | `45369 <https:////gerrit.fd.io/r/c/vpp/+/45369>`_ [VECr 0]: ikev2: switch plugin logging to vlib_log
  | `45368 <https:////gerrit.fd.io/r/c/vpp/+/45368>`_ [VECr 0]: ikev2: avoid mutating shared transform descriptors
  | `45366 <https:////gerrit.fd.io/r/c/vpp/+/45366>`_ [VECr 0]: ikev2: add AES-CMAC PRF support

interface: **Dave Barach** <vpp@barachs.net>
  | `45296 <https:////gerrit.fd.io/r/c/vpp/+/45296>`_ [VECr 8]: ethernet: implement outer_vlan_id_any sub-interface matching
  | `45262 <https:////gerrit.fd.io/r/c/vpp/+/45262>`_ [VECr 13]: interface: add global default rx-mode setting

ip-neighbor: **Neale Ranns** <neale@graphiant.com>
  | `44479 <https:////gerrit.fd.io/r/c/vpp/+/44479>`_ [VECr 2]: ip: add interface address change notifications
  | `42150 <https:////gerrit.fd.io/r/c/vpp/+/42150>`_ [VECr 5]: tests: reduce sleep interval in ip-neighbor age test
  | `45012 <https:////gerrit.fd.io/r/c/vpp/+/45012>`_ [VECr 11]: ip-neighbor: suppress off-link adj-fib on addressed interfaces

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `44948 <https:////gerrit.fd.io/r/c/vpp/+/44948>`_ [VECr 0]: ip6: fix show ip6-ll cli if selector
  | `44479 <https:////gerrit.fd.io/r/c/vpp/+/44479>`_ [VECr 2]: ip: add interface address change notifications
  | `45280 <https:////gerrit.fd.io/r/c/vpp/+/45280>`_ [VECr 8]: gso: implement IPv6 extension header traversal
  | `45260 <https:////gerrit.fd.io/r/c/vpp/+/45260>`_ [VECr 13]: ip6-nd: add per-interface control for inbound RA acceptance
  | `42958 <https:////gerrit.fd.io/r/c/vpp/+/42958>`_ [VECr 22]: tm: add 'mark_flow' action for traffic management

ip6-nd: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `44966 <https:////gerrit.fd.io/r/c/vpp/+/44966>`_ [VECr 6]: ip-neighbor: fix missing solicited-node multicast MAC
  | `45268 <https:////gerrit.fd.io/r/c/vpp/+/45268>`_ [VECr 13]: ip6-nd: enforce on-link source validation for RS neighbor learning
  | `45074 <https:////gerrit.fd.io/r/c/vpp/+/45074>`_ [VECr 13]: ip6-nd: enforce on-link source validation for ND learning
  | `45046 <https:////gerrit.fd.io/r/c/vpp/+/45046>`_ [VECr 13]: ip6-nd: add punt reason for neigh advs
  | `45260 <https:////gerrit.fd.io/r/c/vpp/+/45260>`_ [VECr 13]: ip6-nd: add per-interface control for inbound RA acceptance
  | `44350 <https:////gerrit.fd.io/r/c/vpp/+/44350>`_ [VECr 18]: ip6-nd: fix unicast NA handling in ND proxy
  | `45099 <https:////gerrit.fd.io/r/c/vpp/+/45099>`_ [VECr 19]: ip6-nd: add nd-proxy all dst

ipsec: **Neale Ranns** <neale@graphiant.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `45113 <https:////gerrit.fd.io/r/c/vpp/+/45113>`_ [VECr 25]: ipsec: fix implicit enum cast warnings with GCC 15

l2: **John Lo** <lojultra2020@outlook.com>, **Steven Luong** <sluong@cisco.com>
  | `44858 <https:////gerrit.fd.io/r/c/vpp/+/44858>`_ [VECr 0]: l2: fix missing CDP hello packets on BVI interface
  | `45296 <https:////gerrit.fd.io/r/c/vpp/+/45296>`_ [VECr 8]: ethernet: implement outer_vlan_id_any sub-interface matching

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `45349 <https:////gerrit.fd.io/r/c/vpp/+/45349>`_ [VECr 4]: linux-cp: fix memory leak in default netns command
  | `45271 <https:////gerrit.fd.io/r/c/vpp/+/45271>`_ [VECr 12]: linux-cp: prevent MAC address sync on non-Ethernet interfaces on RTM_NEWLINK

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `45033 <https:////gerrit.fd.io/r/c/vpp/+/45033>`_ [VECr 0]: af_xdp: add support for multi-buffer
  | `45374 <https:////gerrit.fd.io/r/c/vpp/+/45374>`_ [VECr 1]: build rpm-packaging: make vpp rpm package for kylinV11
  | `44479 <https:////gerrit.fd.io/r/c/vpp/+/44479>`_ [VECr 2]: ip: add interface address change notifications
  | `45315 <https:////gerrit.fd.io/r/c/vpp/+/45315>`_ [VECr 4]: ttl-fixup: add new plugin to support transparent host forwarding
  | `45042 <https:////gerrit.fd.io/r/c/vpp/+/45042>`_ [VECr 13]: stats: stat_segment_ls_r() only return NULL on error
  | `45043 <https:////gerrit.fd.io/r/c/vpp/+/45043>`_ [VECr 13]: stats: don't leak regcomp() allocated memory
  | `45119 <https:////gerrit.fd.io/r/c/vpp/+/45119>`_ [VECr 25]: build: add Fedora 43 build compatibility

octeon: **Monendra Singh Kushwaha** <kmonendra@marvell.com>, **Damjan Marion** <damarion@cisco.com>
  | `42257 <https:////gerrit.fd.io/r/c/vpp/+/42257>`_ [VECr 22]: octeon: implement hardware traffic management

pg: **Dave Barach** <vpp@barachs.net>
  | `45280 <https:////gerrit.fd.io/r/c/vpp/+/45280>`_ [VECr 8]: gso: implement IPv6 extension header traversal

policer: **Neale Ranns** <neale@graphiant.com>, **Maxime Peim** <maxime.peim@gmail.com>
  | `45249 <https:////gerrit.fd.io/r/c/vpp/+/45249>`_ [VECr 14]: policer: fix DSCP marking for VLAN-tagged packets
  | `45252 <https:////gerrit.fd.io/r/c/vpp/+/45252>`_ [VECr 14]: policer: fix unchecked policer removal
  | `45254 <https:////gerrit.fd.io/r/c/vpp/+/45254>`_ [VECr 14]: policer: reject deletion of policer used by punt policing
  | `45203 <https:////gerrit.fd.io/r/c/vpp/+/45203>`_ [VECr 19]: policer: avoid redundant l2_overhead array access on TX path

sasc: **Ole Troan** <otroan@employees.org>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `45115 <https:////gerrit.fd.io/r/c/vpp/+/45115>`_ [VECr 25]: sasc: fix maybe-uninitialized warning with GCC 15

sfdp: **Mohammed Hawari** <mohammed@hawari.fr>, **Hadi Rayan Al-Sandid** <halsandi@cisco.com>, **Guillaume Solignac** <gsoligna@cisco.com>, **Ole Troan** <otroan@employees.org>
  | `45101 <https:////gerrit.fd.io/r/c/vpp/+/45101>`_ [VECr 0]: sfdp: guard packet bit shifts in lookup
  | `44976 <https:////gerrit.fd.io/r/c/vpp/+/44976>`_ [VECr 1]: sfdp: offload lookup via vnet flow mark

sfdp_services: **Mohammed Hawari** <mohammed@hawari.fr>, **Hadi Rayan Al-Sandid** <halsandi@cisco.com>, **Guillaume Solignac** <gsoligna@cisco.com>, **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>
  | `44976 <https:////gerrit.fd.io/r/c/vpp/+/44976>`_ [VECr 1]: sfdp: offload lookup via vnet flow mark
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 4]: sfdp: add sfdp-session-stats service
  | `45177 <https:////gerrit.fd.io/r/c/vpp/+/45177>`_ [VECr 19]: sfdp: add blacklist/whitelist to snort service

snort: **Damjan Marion** <damarion@cisco.com>
  | `44923 <https:////gerrit.fd.io/r/c/vpp/+/44923>`_ [VECr 13]: snort: copy metadata from original to generated packets
  | `44919 <https:////gerrit.fd.io/r/c/vpp/+/44919>`_ [VECr 13]: snort: fix inject/finalize ordering race in deq node
  | `45177 <https:////gerrit.fd.io/r/c/vpp/+/45177>`_ [VECr 19]: sfdp: add blacklist/whitelist to snort service
  | `45116 <https:////gerrit.fd.io/r/c/vpp/+/45116>`_ [VECr 25]: snort: fix maybe-uninitialized warning with GCC 15

tap: **Damjan Marion** <damarion@cisco.com>, **Steven Luong** <sluong@cisco.com>, **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>
  | `45280 <https:////gerrit.fd.io/r/c/vpp/+/45280>`_ [VECr 8]: gso: implement IPv6 extension header traversal
  | `45262 <https:////gerrit.fd.io/r/c/vpp/+/45262>`_ [VECr 13]: interface: add global default rx-mode setting

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `45381 <https:////gerrit.fd.io/r/c/vpp/+/45381>`_ [VECr 0]: linux-cp: add more namespace-based tests
  | `45033 <https:////gerrit.fd.io/r/c/vpp/+/45033>`_ [VECr 0]: af_xdp: add support for multi-buffer
  | `45364 <https:////gerrit.fd.io/r/c/vpp/+/45364>`_ [VECr 0]: ikev2: add AES-CTR child SA support
  | `45367 <https:////gerrit.fd.io/r/c/vpp/+/45367>`_ [VECr 0]: ikev2: add AES-CMAC integrity support
  | `45363 <https:////gerrit.fd.io/r/c/vpp/+/45363>`_ [VECr 0]: ikev2: add null encryption support
  | `45369 <https:////gerrit.fd.io/r/c/vpp/+/45369>`_ [VECr 0]: ikev2: switch plugin logging to vlib_log
  | `45366 <https:////gerrit.fd.io/r/c/vpp/+/45366>`_ [VECr 0]: ikev2: add AES-CMAC PRF support
  | `42486 <https:////gerrit.fd.io/r/c/vpp/+/42486>`_ [VECr 0]: tests: add send_and_expect_multi
  | `43369 <https:////gerrit.fd.io/r/c/vpp/+/43369>`_ [VECr 1]: cnat: support encapsulation and session cleanup on backend deletion
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 4]: sfdp: add sfdp-session-stats service
  | `42150 <https:////gerrit.fd.io/r/c/vpp/+/42150>`_ [VECr 5]: tests: reduce sleep interval in ip-neighbor age test
  | `44966 <https:////gerrit.fd.io/r/c/vpp/+/44966>`_ [VECr 6]: ip-neighbor: fix missing solicited-node multicast MAC
  | `45296 <https:////gerrit.fd.io/r/c/vpp/+/45296>`_ [VECr 8]: ethernet: implement outer_vlan_id_any sub-interface matching
  | `45280 <https:////gerrit.fd.io/r/c/vpp/+/45280>`_ [VECr 8]: gso: implement IPv6 extension header traversal
  | `45012 <https:////gerrit.fd.io/r/c/vpp/+/45012>`_ [VECr 11]: ip-neighbor: suppress off-link adj-fib on addressed interfaces
  | `45268 <https:////gerrit.fd.io/r/c/vpp/+/45268>`_ [VECr 13]: ip6-nd: enforce on-link source validation for RS neighbor learning
  | `45073 <https:////gerrit.fd.io/r/c/vpp/+/45073>`_ [VECr 13]: fib: honor unnumbered RX interface in MFIB RPF check
  | `45074 <https:////gerrit.fd.io/r/c/vpp/+/45074>`_ [VECr 13]: ip6-nd: enforce on-link source validation for ND learning
  | `45046 <https:////gerrit.fd.io/r/c/vpp/+/45046>`_ [VECr 13]: ip6-nd: add punt reason for neigh advs
  | `45260 <https:////gerrit.fd.io/r/c/vpp/+/45260>`_ [VECr 13]: ip6-nd: add per-interface control for inbound RA acceptance
  | `45249 <https:////gerrit.fd.io/r/c/vpp/+/45249>`_ [VECr 14]: policer: fix DSCP marking for VLAN-tagged packets
  | `45252 <https:////gerrit.fd.io/r/c/vpp/+/45252>`_ [VECr 14]: policer: fix unchecked policer removal
  | `45254 <https:////gerrit.fd.io/r/c/vpp/+/45254>`_ [VECr 14]: policer: reject deletion of policer used by punt policing
  | `44350 <https:////gerrit.fd.io/r/c/vpp/+/44350>`_ [VECr 18]: ip6-nd: fix unicast NA handling in ND proxy
  | `45099 <https:////gerrit.fd.io/r/c/vpp/+/45099>`_ [VECr 19]: ip6-nd: add nd-proxy all dst
  | `45058 <https:////gerrit.fd.io/r/c/vpp/+/45058>`_ [VECr 20]: flowprobe: count based sampling support

unittest: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `45280 <https:////gerrit.fd.io/r/c/vpp/+/45280>`_ [VECr 8]: gso: implement IPv6 extension header traversal

vcl: **Florin Coras** <fcoras@cisco.com>
  | `44450 <https:////gerrit.fd.io/r/c/vpp/+/44450>`_ [VECr 0]: misc: patch to test CI infra

virtio: **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>, **Damjan Marion** <damarion@cisco.com>
  | `45280 <https:////gerrit.fd.io/r/c/vpp/+/45280>`_ [VECr 8]: gso: implement IPv6 extension header traversal
  | `45262 <https:////gerrit.fd.io/r/c/vpp/+/45262>`_ [VECr 13]: interface: add global default rx-mode setting

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `43538 <https:////gerrit.fd.io/r/c/vpp/+/43538>`_ [VECr 0]: stats: show raw value in show stat segment

vpp: **Dave Barach** <vpp@barachs.net>
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 4]: sfdp: add sfdp-session-stats service

vppapigen: **Ole Troan** <otroan@employees.org>
  | `44546 <https:////gerrit.fd.io/r/c/vpp/+/44546>`_ [VECr 12]: vppapigen: error on use of array with unspecified length
  | `44551 <https:////gerrit.fd.io/r/c/vpp/+/44551>`_ [VECr 12]: vppapigen: fix inconsistency in paths JSON

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `44519 <https:////gerrit.fd.io/r/c/vpp/+/44519>`_ [VECr 7]: vppinfra: format_hexdump_trunc, unformat_bitrate, format_backtrace

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Akos Orban** <orbanakos2001@gmail.com>:

  | `45001 <https:////gerrit.fd.io/r/c/vpp/+/45001>`_ [VeC 35]: cnat: fix show cnat translation for specific translation id
  | `44995 <https:////gerrit.fd.io/r/c/vpp/+/44995>`_ [VeC 35]: cnat: fix show cnat client showing invalid for client id

**Alexander Chernavin** <chernavin@mts.ru>:

  | `43726 <https:////gerrit.fd.io/r/c/vpp/+/43726>`_ [vEc 0]: vhost: fix rxvq interrupts triggered because of race

**Andrew Mason** <mason12@gmail.com>:

  | `44082 <https:////gerrit.fd.io/r/c/vpp/+/44082>`_ [vec 145]: linux-cp: Punt for ISIS traffic over linux-cp plugin
  | `44085 <https:////gerrit.fd.io/r/c/vpp/+/44085>`_ [veC 145]: linux-cp: Punt for ISIS traffic over linux-cp plugin

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `41210 <https:////gerrit.fd.io/r/c/vpp/+/41210>`_ [veC 69]: build: disable the "new" way of handling API dependencies which relies on a broken CMake feature

**Anna Neiman** <anna.neiman@insidepacket.com>:

  | `43046 <https:////gerrit.fd.io/r/c/vpp/+/43046>`_ [VeC 97]: feature: Call dvr_dpo_unlock in case delete SW interface - in order enable feature ip4-dvr-reinject on the following addition interface ;add arch index in show features
  | `43916 <https:////gerrit.fd.io/r/c/vpp/+/43916>`_ [Vec 158]: vlib: print non-parked threads on vlib_worker_thread_barrier_sync_int
  | `43915 <https:////gerrit.fd.io/r/c/vpp/+/43915>`_ [Vec 161]: vnet: Initialize the classify arrays to ~0

**Aritra Basu** <aritrbas@cisco.com>:

  | `44981 <https:////gerrit.fd.io/r/c/vpp/+/44981>`_ [VeC 39]: ip-neighbor: preserve interface LL receive DPO for self link-local

**Bartlomiej Leszak** <bartlomiej.leszak@gmail.com>:

  | `42978 <https:////gerrit.fd.io/r/c/vpp/+/42978>`_ [VeC 97]: pnat: do not disable pnat on rule deletion

**Benoît Ganne** <bganne@cisco.com>:

  | `39443 <https:////gerrit.fd.io/r/c/vpp/+/39443>`_ [veC 32]: vnet: reorder vnet_buffer2 metadata
  | `44962 <https:////gerrit.fd.io/r/c/vpp/+/44962>`_ [VeC 41]: pppoe: initialize sw_if_index before early goto

**C.J. Collier**:

  | `1948 <https:////gerrit.fd.io/r/c/vpp/+/1948>`_ [veC 159]: DO NOT MERGE - testing new build image

**Damjan Marion** <dmarion@0xa5.net>:

  | `45365 <https:////gerrit.fd.io/r/c/vpp/+/45365>`_ [vEC 0]: ikev2: add AES-GMAC child SA support
  | `44964 <https:////gerrit.fd.io/r/c/vpp/+/44964>`_ [VeC 40]: ethernet: add RSS callbacks
  | `44092 <https:////gerrit.fd.io/r/c/vpp/+/44092>`_ [veC 139]: ipsec: precompute payload and payload length adjustments
  | `44081 <https:////gerrit.fd.io/r/c/vpp/+/44081>`_ [veC 144]: ipsec: fill op templates with lengths and tag sizes

**Dmitriy Vakhrushev** <dvakhrushev@netgate.com>:

  | `45379 <https:////gerrit.fd.io/r/c/vpp/+/45379>`_ [VEc 0]: af_xdp: Add mac-reuse option to reuse interface's HW MAC address

**FDio GitHub Actions** <releng+fdio-github@linuxfoundation.org>:

  | `45227 <https:////gerrit.fd.io/r/c/vpp/+/45227>`_ [vEC 15]: build(deps): bump step-security/harden-runner from 2.13.2 to 2.16.0
  | `45225 <https:////gerrit.fd.io/r/c/vpp/+/45225>`_ [vEC 15]: build(deps): bump lfreleng-actions/github2gerrit-action from 1.0.5 to 1.0.8

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `44847 <https:////gerrit.fd.io/r/c/vpp/+/44847>`_ [Vec 36]: sfdp: modify tenant_index type from u16 to u32
  | `44474 <https:////gerrit.fd.io/r/c/vpp/+/44474>`_ [Vec 83]: sasc: fix tenant_index overlap in sasc_buffer

**Ivan Ivanets** <iivanets@cisco.com>:

  | `44827 <https:////gerrit.fd.io/r/c/vpp/+/44827>`_ [VeC 34]: crypto: unify per-thread key_data allocation
  | `43891 <https:////gerrit.fd.io/r/c/vpp/+/43891>`_ [veC 168]: tests: add crypto+hmac perf test

**Jerome Labidurie** <jerome.labidurie@orange.com>:

  | `44849 <https:////gerrit.fd.io/r/c/vpp/+/44849>`_ [VeC 53]: policer: api to unaply policer from any interface
  | `44844 <https:////gerrit.fd.io/r/c/vpp/+/44844>`_ [VeC 53]: policer: prevent policer to be applied twice
  | `44843 <https:////gerrit.fd.io/r/c/vpp/+/44843>`_ [VeC 53]: policer: fix crash when unapplying a policer
  | `44693 <https:////gerrit.fd.io/r/c/vpp/+/44693>`_ [VeC 53]: policer: obtain policers applied to an interface

**Jerome Tollet** <jtollet@cisco.com>:

  | `45102 <https:////gerrit.fd.io/r/c/vpp/+/45102>`_ [vEc 0]: sfdp: add configurable timer interval and fix kill immediacy
  | `44559 <https:////gerrit.fd.io/r/c/vpp/+/44559>`_ [VEc 28]: af_xdp: ensure null termination in format() string outputs
  | `44584 <https:////gerrit.fd.io/r/c/vpp/+/44584>`_ [veC 68]: tests: fix tag_fixme_debian12 to tag_fixme_debian11
  | `44572 <https:////gerrit.fd.io/r/c/vpp/+/44572>`_ [VeC 80]: virtio: add native plugin L2 xconnect test with QEMU

**Jiajun Liang** <3138947285@qq.com>:

  | `45289 <https:////gerrit.fd.io/r/c/vpp/+/45289>`_ [VEc 0]: pppoe: add PPPoE client and pppox

**Jing Peng** <jing@meter.com>:

  | `37058 <https:////gerrit.fd.io/r/c/vpp/+/37058>`_ [VeC 55]: vppapigen: fix json build error

**Maxime Peim** <maxime.peim@gmail.com>:

  | `44972 <https:////gerrit.fd.io/r/c/vpp/+/44972>`_ [vEC 1]: dpdk: call flow configure on device setup
  | `45312 <https:////gerrit.fd.io/r/c/vpp/+/45312>`_ [vEC 6]: sfdp: fix timer macro usage
  | `45253 <https:////gerrit.fd.io/r/c/vpp/+/45253>`_ [vEC 14]: policer: reject delete of policer still applied to interface
  | `43515 <https:////gerrit.fd.io/r/c/vpp/+/43515>`_ [Vec 167]: ping: introduce traceroute tool

**Mohammad Mahdi Nemati Haravani** <nemati.mahdi255@gmail.com>:

  | `44303 <https:////gerrit.fd.io/r/c/vpp/+/44303>`_ [VeC 112]: build: fix etc path for vpp-ext-deps package fix the bug vpp ext deb for DPDK 25.07 and MLX5 PMD topic

**Mohammed HAWARI** <momohawari@gmail.com>:

  | `42343 <https:////gerrit.fd.io/r/c/vpp/+/42343>`_ [VeC 111]: vcl: LDP default to regular option
  | `43874 <https:////gerrit.fd.io/r/c/vpp/+/43874>`_ [Vec 165]: unittest: add sfdp testing and unity framework

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `44935 <https:////gerrit.fd.io/r/c/vpp/+/44935>`_ [VEc 13]: virtio: add support for mac filtering
  | `44930 <https:////gerrit.fd.io/r/c/vpp/+/44930>`_ [VEc 13]: virtio: add support for mac address changing
  | `42886 <https:////gerrit.fd.io/r/c/vpp/+/42886>`_ [VeC 42]: ipip: fix support for ipip6o6 from linux tunnel
  | `44715 <https:////gerrit.fd.io/r/c/vpp/+/44715>`_ [Vec 46]: pg: Guard against non‑monotonic time and negative accumulator
  | `44426 <https:////gerrit.fd.io/r/c/vpp/+/44426>`_ [VeC 81]: virtio: add the check if MAC feature is negotiated

**Moinak Bhattacharyya** <moinakb001@gmail.com>:

  | `44708 <https:////gerrit.fd.io/r/c/vpp/+/44708>`_ [VeC 59]: iouring: Add io_uring plugin to allow polling usage of io_uring
  | `43610 <https:////gerrit.fd.io/r/c/vpp/+/43610>`_ [Vec 176]: af_xdp: allow usage of dynamic libbpf and libxdp
  | `43606 <https:////gerrit.fd.io/r/c/vpp/+/43606>`_ [Vec 176]: af_xdp: introduce flag to allow SKB mode

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `44903 <https:////gerrit.fd.io/r/c/vpp/+/44903>`_ [VeC 36]: vxlan: reset next_dpo on delete
  | `44961 <https:////gerrit.fd.io/r/c/vpp/+/44961>`_ [Vec 41]: ip6-nd: support RA pfx info option with flag L&!A

**Parth Sahu** <parthsahu15@gmail.com>:

  | `44813 <https:////gerrit.fd.io/r/c/vpp/+/44813>`_ [VeC 60]: session auto_sdl: fix SDL show rule argument order
  | `44796 <https:////gerrit.fd.io/r/c/vpp/+/44796>`_ [veC 62]: fix: correct fixstyle in session_sdl command function

**Ryosuke Nakayama** <ryosuke_666@icloud.com>:

  | `45117 <https:////gerrit.fd.io/r/c/vpp/+/45117>`_ [vEC 25]: atlantic: remove unused pkt_n_desc variable

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `44230 <https:////gerrit.fd.io/r/c/vpp/+/44230>`_ [vEC 0]: linux-cp: bind lcp_router_table lifetime to lcp_itf_pair
  | `44232 <https:////gerrit.fd.io/r/c/vpp/+/44232>`_ [VeC 95]: linux-cp: fix cleanup of special routes
  | `44241 <https:////gerrit.fd.io/r/c/vpp/+/44241>`_ [Vec 103]: linux-cp: on remove do cleanup for all fibs
  | `44249 <https:////gerrit.fd.io/r/c/vpp/+/44249>`_ [VeC 118]: fib: dump by src not only contributing routes

**Venkata Ravichandra Mynidi** <vmynidi@marvell.com>:

  | `40775 <https:////gerrit.fd.io/r/c/vpp/+/40775>`_ [VEc 6]: tm: add tm framework for hw traffic management

**Vladimir Zhigulin** <vladimir.jigulin@travelping.com>:

  | `40145 <https:////gerrit.fd.io/r/c/vpp/+/40145>`_ [vEC 0]: vppinfra: collect heap stats in constant time

**Vladislav Grishenko** <themiron@mail.ru>:

  | `44575 <https:////gerrit.fd.io/r/c/vpp/+/44575>`_ [VeC 81]: fib: add interface-rx dpo mpls support
  | `44574 <https:////gerrit.fd.io/r/c/vpp/+/44574>`_ [VeC 81]: fib: fix stale interface-rx dpo fib after deag/lookup
  | `41660 <https:////gerrit.fd.io/r/c/vpp/+/41660>`_ [VeC 81]: nat: add nat44-ed ipfix dst address and port logging
  | `42538 <https:////gerrit.fd.io/r/c/vpp/+/42538>`_ [VeC 81]: nat: speedup nat44-ed vrf table lookups
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VeC 81]: nat: fix nat44-ed address removal from fib
  | `44563 <https:////gerrit.fd.io/r/c/vpp/+/44563>`_ [veC 82]: ip: fix DSCP CS7 value
  | `44568 <https:////gerrit.fd.io/r/c/vpp/+/44568>`_ [VeC 82]: vxlan: add default dscp value config for vxlan encap
  | `44567 <https:////gerrit.fd.io/r/c/vpp/+/44567>`_ [VeC 82]: udp: add default dscp value config for udp encap
  | `40627 <https:////gerrit.fd.io/r/c/vpp/+/40627>`_ [VeC 82]: fib: fix invalid udp encap id cases
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VeC 82]: fib: fix udp encap mp-safe ops and id validation
  | `43180 <https:////gerrit.fd.io/r/c/vpp/+/43180>`_ [VeC 82]: fib: avoid loadbalance dpo node path polarisation
  | `40630 <https:////gerrit.fd.io/r/c/vpp/+/40630>`_ [VeC 82]: vlib: mark cli quit command as mp_safe

**Xiangqing Cheng** <chengxq@chinatelecom.cn>:

  | `42849 <https:////gerrit.fd.io/r/c/vpp/+/42849>`_ [VeC 97]: ip-neighbor: ARP/NA per-interface counter improvements

**joydeep ghosh** <joydeep779@gmail.com>:

  | `44631 <https:////gerrit.fd.io/r/c/vpp/+/44631>`_ [vec 49]: dns: fix crash when no usable source address exists

**lei feng** <1579628578@qq.com>:

  | `42077 <https:////gerrit.fd.io/r/c/vpp/+/42077>`_ [VEc 0]: dns: dns request ip6 fix
  | `42129 <https:////gerrit.fd.io/r/c/vpp/+/42129>`_ [VEc 0]: dns: support ipv6 server to resolve name
  | `42064 <https:////gerrit.fd.io/r/c/vpp/+/42064>`_ [vec 54]: docs: Python apis examples

**mahdi varasteh** <mahdy.varasteh@gmail.com>:

  | `43892 <https:////gerrit.fd.io/r/c/vpp/+/43892>`_ [VeC 106]: fib: compute fib entry flags from full path list

**niklesh** <nikleshparshaboina@gmail.com>:

  | `45016 <https:////gerrit.fd.io/r/c/vpp/+/45016>`_ [VEc 0]: cnat: add scope_id to session key

**pkt4u** <pkt4u@outlook.com>:

  | `44208 <https:////gerrit.fd.io/r/c/vpp/+/44208>`_ [vEC 0]: lb: fix API byte order and IPv4 prefix length handling
  | `44207 <https:////gerrit.fd.io/r/c/vpp/+/44207>`_ [VeC 94]: lb: fix incorrect byte order conversion for vip port display

**ruici wang** <964491902@qq.com>:

  | `44100 <https:////gerrit.fd.io/r/c/vpp/+/44100>`_ [veC 139]: ipsec: prevent use of deleted keys in async mode

**shaohui jin** <jinshaohui789@163.com>:

  | `44928 <https:////gerrit.fd.io/r/c/vpp/+/44928>`_ [vEC 27]: fib: IPv4 Route Query Command Crash

**steven luong** <sluong@cisco.com>:

  | `44569 <https:////gerrit.fd.io/r/c/vpp/+/44569>`_ [VeC 82]: vppinfra: clib_time_verify_frequency may cause time jump

**yelena_c@rad.com** <yelena_c@rad.com>:

  | `44536 <https:////gerrit.fd.io/r/c/vpp/+/44536>`_ [veC 64]: hs-test: fix CI infra issues
  | `44421 <https:////gerrit.fd.io/r/c/vpp/+/44421>`_ [VeC 64]: l2: fix null pointer access in l2-efp-filter

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
authors          87
maintainers      68
committers       0
abandoned        0
================ ===

