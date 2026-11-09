
==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Monday 2026-11-09, 07:54:03
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

  | `47239 <https:////gerrit.fd.io/r/c/vpp/+/47239>`_ [VECR 0]: tests: fix core lookup with absolute core_pattern

Maintainers:
------------
| **Please review these gerrit changes.**

| **NOTE: Gerrit changes may be included under more than one feature based on the modified files regardless of the feature list included on the commit headline.**

acl: **Andrew Yourtchenko** <ayourtch@gmail.com>
  | `47511 <https:////gerrit.fd.io/r/c/vpp/+/47511>`_ [VECr 1]: acl: bound collision-list rescans on no-op split
  | `47058 <https:////gerrit.fd.io/r/c/vpp/+/47058>`_ [VECr 23]: acl: stop counting hash hits in a shared per-entry field

af_packet: **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>
  | `47515 <https:////gerrit.fd.io/r/c/vpp/+/47515>`_ [VECr 1]: af_packet: restore 802.1ad tags with the correct TPID

api: **Dave Barach** <vpp@barachs.net>
  | `47209 <https:////gerrit.fd.io/r/c/vpp/+/47209>`_ [VECr 13]: api: align shared-memory API handler calls
  | `47210 <https:////gerrit.fd.io/r/c/vpp/+/47210>`_ [VECr 13]: api: use unsigned socket handle bit

arp: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `47276 <https:////gerrit.fd.io/r/c/vpp/+/47276>`_ [VECr 13]: arp: fix reply for local address with adj-fib

bfd: **Klement Sekera** <klement.sekera@gmail.com>
  | `47425 <https:////gerrit.fd.io/r/c/vpp/+/47425>`_ [VECr 5]: bfd: add S-BFD reflector datapath
  | `47426 <https:////gerrit.fd.io/r/c/vpp/+/47426>`_ [VECr 5]: bfd: reflect S-BFD requests sent over MPLS paths
  | `47423 <https:////gerrit.fd.io/r/c/vpp/+/47423>`_ [VECr 5]: bfd: add S-BFD reflector configuration
  | `47427 <https:////gerrit.fd.io/r/c/vpp/+/47427>`_ [VECr 5]: bfd: document the S-BFD reflector

buffers: **Damjan Marion** <damarion@cisco.com>, **Dave Barach** <vpp@barachs.net>
  | `47321 <https:////gerrit.fd.io/r/c/vpp/+/47321>`_ [VECr 10]: vlib: add helper to check available headroom in vlib_buffer_t

build: **Damjan Marion** <damarion@cisco.com>
  | `46907 <https:////gerrit.fd.io/r/c/vpp/+/46907>`_ [VECr 10]: fastacl: RFC 8955 FlowSpec filter for volumetric DDoS mitigation
  | `47270 <https:////gerrit.fd.io/r/c/vpp/+/47270>`_ [VECr 14]: build: refresh optional SPDK upstream snapshot

dhcp: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `47514 <https:////gerrit.fd.io/r/c/vpp/+/47514>`_ [VECr 1]: dhcp: bound client option parsing to the packet
  | `47281 <https:////gerrit.fd.io/r/c/vpp/+/47281>`_ [VECr 13]: dhcp: fix PD client crash without link-local
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 13]: pppoeclient: add PPPoE client plugin with DHCPv6 observability

dispatch-trace: **Dave Barach** <vpp@barachs.net>
  | `46469 <https:////gerrit.fd.io/r/c/vpp/+/46469>`_ [VECr 18]: dispatch-trace: fix SIGSEGV on multi-worker handoff

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `45941 <https:////gerrit.fd.io/r/c/vpp/+/45941>`_ [VECr 1]: misc: patch to test CI infra
  | `46527 <https:////gerrit.fd.io/r/c/vpp/+/46527>`_ [VECr 2]: lb: add NAT6_NOPORT encap type
  | `45505 <https:////gerrit.fd.io/r/c/vpp/+/45505>`_ [VECr 3]: rdma: add mlx5 dv tso support for raw packet tx
  | `47423 <https:////gerrit.fd.io/r/c/vpp/+/47423>`_ [VECr 5]: bfd: add S-BFD reflector configuration
  | `47427 <https:////gerrit.fd.io/r/c/vpp/+/47427>`_ [VECr 5]: bfd: document the S-BFD reflector
  | `47274 <https:////gerrit.fd.io/r/c/vpp/+/47274>`_ [VECr 6]: freebsd-cp: FreeBSD Control Plane plugin similar to Linux CP plugin but siginificantly simplified
  | `46907 <https:////gerrit.fd.io/r/c/vpp/+/46907>`_ [VECr 10]: fastacl: RFC 8955 FlowSpec filter for volumetric DDoS mitigation
  | `47298 <https:////gerrit.fd.io/r/c/vpp/+/47298>`_ [VECr 11]: misc: VPP 26.10 Release Notes
  | `46461 <https:////gerrit.fd.io/r/c/vpp/+/46461>`_ [VECr 12]: ipsec: IPTFS (RFC 9347)
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 13]: pppoeclient: add PPPoE client plugin with DHCPv6 observability

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `47480 <https:////gerrit.fd.io/r/c/vpp/+/47480>`_ [VECr 2]: dpdk: fix alignment of rx and tx trace records
  | `46828 <https:////gerrit.fd.io/r/c/vpp/+/46828>`_ [VECr 3]: dpdk: fix change mac address of the member failed
  | `46939 <https:////gerrit.fd.io/r/c/vpp/+/46939>`_ [VECr 4]: dpdk: don't leak chained mbufs when multi-seg is disabled
  | `47213 <https:////gerrit.fd.io/r/c/vpp/+/47213>`_ [VECr 5]: dpdk: read transceiver EEPROM asynchronously, never under the barrier
  | `45675 <https:////gerrit.fd.io/r/c/vpp/+/45675>`_ [VECr 13]: dpdk: log MFIB MAC replay tolerance at debug level
  | `47200 <https:////gerrit.fd.io/r/c/vpp/+/47200>`_ [VECr 17]: dpdk: fix clib file descriptor leak on admin down
  | `46953 <https:////gerrit.fd.io/r/c/vpp/+/46953>`_ [VECr 30]: dpdk: recognise the the MANA VF as a bifurcated device

dpdk-cryptodev: **Kai Ji** <kai.ji@intel.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `47522 <https:////gerrit.fd.io/r/c/vpp/+/47522>`_ [VECr 1]: dpdk: fix cryptodev thread assignment CLI

drivers: **Damjan Marion** <damarion@cisco.com>
  | `47538 <https:////gerrit.fd.io/r/c/vpp/+/47538>`_ [VECr 0]: atlantic: count rx buffer allocation failures
  | `47553 <https:////gerrit.fd.io/r/c/vpp/+/47553>`_ [VECr 0]: ige: program the primary mac address on start
  | `47539 <https:////gerrit.fd.io/r/c/vpp/+/47539>`_ [VECr 0]: atlantic: fix promiscuous mode change
  | `47550 <https:////gerrit.fd.io/r/c/vpp/+/47550>`_ [VECr 0]: ige: add tcp segmentation offload
  | `47541 <https:////gerrit.fd.io/r/c/vpp/+/47541>`_ [VECr 0]: ige: use node errors in tx trace
  | `47554 <https:////gerrit.fd.io/r/c/vpp/+/47554>`_ [VECr 0]: ige: do not hold completed tx buffers
  | `47549 <https:////gerrit.fd.io/r/c/vpp/+/47549>`_ [VECr 0]: ige: power down the phy when the port is stopped
  | `47548 <https:////gerrit.fd.io/r/c/vpp/+/47548>`_ [VECr 0]: ige: poll the link only while the port is started
  | `47416 <https:////gerrit.fd.io/r/c/vpp/+/47416>`_ [VECr 6]: ice: guard cleanup before port registration

ethernet: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `47211 <https:////gerrit.fd.io/r/c/vpp/+/47211>`_ [VECr 13]: ethernet: compare unaligned MAC addresses

feature: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `46461 <https:////gerrit.fd.io/r/c/vpp/+/46461>`_ [VECr 12]: ipsec: IPTFS (RFC 9347)

fib: **Neale Ranns** <neale@graphiant.com>
  | `47293 <https:////gerrit.fd.io/r/c/vpp/+/47293>`_ [VECr 2]: fib: add mfib_entry_get_n_paths helper
  | `47292 <https:////gerrit.fd.io/r/c/vpp/+/47292>`_ [VECr 2]: fib: introduce per-source entry count in mfib
  | `46959 <https:////gerrit.fd.io/r/c/vpp/+/46959>`_ [VECr 2]: linux-cp: free lcp_router_table if 0 routes and no lcp pairs only
  | `47402 <https:////gerrit.fd.io/r/c/vpp/+/47402>`_ [VECr 6]: fib: fix stale importer pointer in attached-export walk
  | `47076 <https:////gerrit.fd.io/r/c/vpp/+/47076>`_ [VECr 23]: fib: decide the glean source by the address it holds
  | `47078 <https:////gerrit.fd.io/r/c/vpp/+/47078>`_ [VECr 25]: fib: swap in the paths of a source new to the entry

hs-test: **Florin Coras** <fcoras@cisco.com>, **Matus Fabian** <matfabia@cisco.com>
  | `47529 <https:////gerrit.fd.io/r/c/vpp/+/47529>`_ [VECr 0]: hsa: fix proxy-lite cross-worker session and fifo cleanup
  | `46907 <https:////gerrit.fd.io/r/c/vpp/+/46907>`_ [VECr 10]: fastacl: RFC 8955 FlowSpec filter for volumetric DDoS mitigation

hsa: **Florin Coras** <fcoras@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>
  | `47529 <https:////gerrit.fd.io/r/c/vpp/+/47529>`_ [VECr 0]: hsa: fix proxy-lite cross-worker session and fifo cleanup

iavf: **Damjan Marion** <damarion@cisco.com>
  | `47413 <https:////gerrit.fd.io/r/c/vpp/+/47413>`_ [VECr 4]: iavf: preserve full tso context payload length
  | `47415 <https:////gerrit.fd.io/r/c/vpp/+/47415>`_ [VECr 4]: iavf: simplify tx descriptor chain handling

ikev2: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Benoît Ganne** <bganne@cisco.com>
  | `47349 <https:////gerrit.fd.io/r/c/vpp/+/47349>`_ [VECr 9]: ikev2: free buffer and still tear down local IKE SA when Delete send fails
  | `46461 <https:////gerrit.fd.io/r/c/vpp/+/46461>`_ [VECr 12]: ipsec: IPTFS (RFC 9347)
  | `47192 <https:////gerrit.fd.io/r/c/vpp/+/47192>`_ [VECr 13]: ikev2: keep GRE protection on Child Delete
  | `47242 <https:////gerrit.fd.io/r/c/vpp/+/47242>`_ [VECr 15]: ikev2: accept responder-initiated Child SA rekey
  | `47194 <https:////gerrit.fd.io/r/c/vpp/+/47194>`_ [VECr 15]: ikev2: allocate Child SA IDs without collision
  | `47247 <https:////gerrit.fd.io/r/c/vpp/+/47247>`_ [VECr 15]: ikev2: accept additional Child SA from responder
  | `47241 <https:////gerrit.fd.io/r/c/vpp/+/47241>`_ [VECr 15]: ikev2: preserve responses across local requests
  | `47214 <https:////gerrit.fd.io/r/c/vpp/+/47214>`_ [VECr 19]: ikev2: configure inbound ESP replay window

interface: **Dave Barach** <vpp@barachs.net>
  | `47213 <https:////gerrit.fd.io/r/c/vpp/+/47213>`_ [VECr 5]: dpdk: read transceiver EEPROM asynchronously, never under the barrier
  | `47237 <https:////gerrit.fd.io/r/c/vpp/+/47237>`_ [VECr 5]: interface: make show hardware-interfaces mp-safe
  | `46749 <https:////gerrit.fd.io/r/c/vpp/+/46749>`_ [VECr 13]: pppoeclient: fix orphan TX nodes and shared rename

ip-neighbor: **Neale Ranns** <neale@graphiant.com>
  | `47273 <https:////gerrit.fd.io/r/c/vpp/+/47273>`_ [VECr 12]: ip-neighbor: add neighbour table event counters
  | `47209 <https:////gerrit.fd.io/r/c/vpp/+/47209>`_ [VECr 13]: api: align shared-memory API handler calls

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `47445 <https:////gerrit.fd.io/r/c/vpp/+/47445>`_ [VECr 0]: ip6: fix show ip6-ll interface selector
  | `47383 <https:////gerrit.fd.io/r/c/vpp/+/47383>`_ [VECr 8]: ip: fix IPv6 SVR total payload length
  | `46461 <https:////gerrit.fd.io/r/c/vpp/+/46461>`_ [VECr 12]: ipsec: IPTFS (RFC 9347)
  | `47209 <https:////gerrit.fd.io/r/c/vpp/+/47209>`_ [VECr 13]: api: align shared-memory API handler calls
  | `45955 <https:////gerrit.fd.io/r/c/vpp/+/45955>`_ [VECr 15]: ip: fix adjacent packet overwrite with ip frags
  | `45954 <https:////gerrit.fd.io/r/c/vpp/+/45954>`_ [VECr 15]: ip: fix adjacent packet overwrite with ip6 frags
  | `46051 <https:////gerrit.fd.io/r/c/vpp/+/46051>`_ [VECr 15]: ip: fix punt socket rx when multiple FDs are ready
  | `47177 <https:////gerrit.fd.io/r/c/vpp/+/47177>`_ [VECr 20]: ip: parse the output-arc IPv6 header in sv-reass update
  | `47172 <https:////gerrit.fd.io/r/c/vpp/+/47172>`_ [VECr 22]: ip: clear l4_hdr_truncated bit in ip4 sv-reass
  | `47173 <https:////gerrit.fd.io/r/c/vpp/+/47173>`_ [VECr 22]: ip: tolerate a NULL total_ip_payload_length in sv-reass lock

ip6-nd: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `45046 <https:////gerrit.fd.io/r/c/vpp/+/45046>`_ [VECr 0]: ip6-nd: make Neighbor Advertisement punting configurable
  | `45099 <https:////gerrit.fd.io/r/c/vpp/+/45099>`_ [VECr 0]: ip6-nd: add all-dst mode to ND mirror proxy
  | `44350 <https:////gerrit.fd.io/r/c/vpp/+/44350>`_ [VECr 0]: ip6-nd: fix unicast NA handling in ND proxy

ipsec: **Neale Ranns** <neale@graphiant.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `46461 <https:////gerrit.fd.io/r/c/vpp/+/46461>`_ [VECr 12]: ipsec: IPTFS (RFC 9347)
  | `47192 <https:////gerrit.fd.io/r/c/vpp/+/47192>`_ [VECr 13]: ikev2: keep GRE protection on Child Delete
  | `47247 <https:////gerrit.fd.io/r/c/vpp/+/47247>`_ [VECr 15]: ikev2: accept additional Child SA from responder

l2: **John Lo** <lojultra2020@outlook.com>, **Steven Luong** <sluong@cisco.com>
  | `47264 <https:////gerrit.fd.io/r/c/vpp/+/47264>`_ [VECr 15]: l2: refuse L3-only bridge and xconnect members

lb: **Pfister** <ppfister@cisco.com>, **Hongjun Ni** <hongjun.ni@intel.com>
  | `46527 <https:////gerrit.fd.io/r/c/vpp/+/46527>`_ [VECr 2]: lb: add NAT6_NOPORT encap type
  | `46526 <https:////gerrit.fd.io/r/c/vpp/+/46526>`_ [VECr 2]: lb: fix NAT66 UDP/IPv6 checksum zero-fold

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `47001 <https:////gerrit.fd.io/r/c/vpp/+/47001>`_ [VECr 0]: linux-cp: add qinq linux to vpp support
  | `47294 <https:////gerrit.fd.io/r/c/vpp/+/47294>`_ [VECr 0]: linux-cp: use special fib/mfib source for special routes
  | `47520 <https:////gerrit.fd.io/r/c/vpp/+/47520>`_ [VECr 1]: linux-cp: release netlink socket and link
  | `47295 <https:////gerrit.fd.io/r/c/vpp/+/47295>`_ [VECr 2]: linux-cp: delete multicast routes from the MFIB
  | `46959 <https:////gerrit.fd.io/r/c/vpp/+/46959>`_ [VECr 2]: linux-cp: free lcp_router_table if 0 routes and no lcp pairs only
  | `47279 <https:////gerrit.fd.io/r/c/vpp/+/47279>`_ [VECr 13]: linux-cp: flush IPv4 routes whenever the host link goes down
  | `47120 <https:////gerrit.fd.io/r/c/vpp/+/47120>`_ [VECr 13]: linux-cp: do not unlock an mfib for MPLS tables
  | `46937 <https:////gerrit.fd.io/r/c/vpp/+/46937>`_ [VECr 13]: linux-cp: only drop a table reference for routes lcp installed
  | `47222 <https:////gerrit.fd.io/r/c/vpp/+/47222>`_ [VECr 15]: linux-cp: avoid a drop path on first route source
  | `46492 <https:////gerrit.fd.io/r/c/vpp/+/46492>`_ [VECr 20]: linux-cp: don't copy an unknown link speed to the host tap

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `47384 <https:////gerrit.fd.io/r/c/vpp/+/47384>`_ [VECr 1]: spdk: remove obsolete RX prototype state
  | `46736 <https:////gerrit.fd.io/r/c/vpp/+/46736>`_ [VECr 1]: spdk: consume fifo-backed deferred rx batches
  | `47423 <https:////gerrit.fd.io/r/c/vpp/+/47423>`_ [VECr 5]: bfd: add S-BFD reflector configuration
  | `47274 <https:////gerrit.fd.io/r/c/vpp/+/47274>`_ [VECr 6]: freebsd-cp: FreeBSD Control Plane plugin similar to Linux CP plugin but siginificantly simplified
  | `46907 <https:////gerrit.fd.io/r/c/vpp/+/46907>`_ [VECr 10]: fastacl: RFC 8955 FlowSpec filter for volumetric DDoS mitigation
  | `46461 <https:////gerrit.fd.io/r/c/vpp/+/46461>`_ [VECr 12]: ipsec: IPTFS (RFC 9347)
  | `46749 <https:////gerrit.fd.io/r/c/vpp/+/46749>`_ [VECr 13]: pppoeclient: fix orphan TX nodes and shared rename
  | `46992 <https:////gerrit.fd.io/r/c/vpp/+/46992>`_ [VECr 13]: pppoeclient: keep control-plane work off workers and pin session VLAN
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 13]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `46993 <https:////gerrit.fd.io/r/c/vpp/+/46993>`_ [VECr 13]: pppoeclient: bind the learned VLAN on the main thread
  | `46991 <https:////gerrit.fd.io/r/c/vpp/+/46991>`_ [VECr 13]: pppoeclient: echo relay tag and accept PADS without AC-Cookie
  | `47263 <https:////gerrit.fd.io/r/c/vpp/+/47263>`_ [VECr 15]: span gre: refuse destinations with no output node

mss_clamp: **Miklos Tirpak** <miklos.tirpak@emnify.com>
  | `47476 <https:////gerrit.fd.io/r/c/vpp/+/47476>`_ [VECr 2]: mss_clamp: reset interface state on interface delete

nat: **Ole Troan** <otroan@employees.org>, **Filip Varga** <fivarga@cisco.com>, **Klement Sekera** <klement.sekera@gmail.com>
  | `47252 <https:////gerrit.fd.io/r/c/vpp/+/47252>`_ [VECr 16]: nat: select dynamic translation by source prefix

nsim: **Dave Barach** <vpp@barachs.net>
  | `47531 <https:////gerrit.fd.io/r/c/vpp/+/47531>`_ [VECr 0]: nsim: trace packets released from scheduler wheels

policer: **Neale Ranns** <neale@graphiant.com>, **Maxime Peim** <maxime.peim@gmail.com>
  | `47209 <https:////gerrit.fd.io/r/c/vpp/+/47209>`_ [VECr 13]: api: align shared-memory API handler calls

quic: **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Florin Coras** <fcoras@cisco.com>
  | `46315 <https:////gerrit.fd.io/r/c/vpp/+/46315>`_ [VECr 16]: quic: quic_quicly add uso support

rdma: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `47443 <https:////gerrit.fd.io/r/c/vpp/+/47443>`_ [VECr 2]: rdma: preserve shared chains in mlx5 SEND
  | `45505 <https:////gerrit.fd.io/r/c/vpp/+/45505>`_ [VECr 3]: rdma: add mlx5 dv tso support for raw packet tx

session: **Florin Coras** <fcoras@cisco.com>
  | `47343 <https:////gerrit.fd.io/r/c/vpp/+/47343>`_ [VECr 0]: session: fix certificate registration race
  | `47521 <https:////gerrit.fd.io/r/c/vpp/+/47521>`_ [VECr 1]: session: fix forced application detach via rpc
  | `47517 <https:////gerrit.fd.io/r/c/vpp/+/47517>`_ [VECr 1]: session: free app on unsupported attach config
  | `47518 <https:////gerrit.fd.io/r/c/vpp/+/47518>`_ [VECr 1]: session: do not double-close rx mq eventfd
  | `46284 <https:////gerrit.fd.io/r/c/vpp/+/46284>`_ [VECr 16]: udp: add segmentation offload support

snort: **Damjan Marion** <damarion@cisco.com>
  | `47231 <https:////gerrit.fd.io/r/c/vpp/+/47231>`_ [VECr 17]: snort: consume the enqueue event before clearing interrupt_pending

span: **N/A
  | `47263 <https:////gerrit.fd.io/r/c/vpp/+/47263>`_ [VECr 15]: span gre: refuse destinations with no output node

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `45046 <https:////gerrit.fd.io/r/c/vpp/+/45046>`_ [VECr 0]: ip6-nd: make Neighbor Advertisement punting configurable
  | `45099 <https:////gerrit.fd.io/r/c/vpp/+/45099>`_ [VECr 0]: ip6-nd: add all-dst mode to ND mirror proxy
  | `47001 <https:////gerrit.fd.io/r/c/vpp/+/47001>`_ [VECr 0]: linux-cp: add qinq linux to vpp support
  | `44350 <https:////gerrit.fd.io/r/c/vpp/+/44350>`_ [VECr 0]: ip6-nd: fix unicast NA handling in ND proxy
  | `47343 <https:////gerrit.fd.io/r/c/vpp/+/47343>`_ [VECr 0]: session: fix certificate registration race
  | `47531 <https:////gerrit.fd.io/r/c/vpp/+/47531>`_ [VECr 0]: nsim: trace packets released from scheduler wheels
  | `47514 <https:////gerrit.fd.io/r/c/vpp/+/47514>`_ [VECr 1]: dhcp: bound client option parsing to the packet
  | `47512 <https:////gerrit.fd.io/r/c/vpp/+/47512>`_ [VECr 1]: ipip: fix test assertions
  | `47513 <https:////gerrit.fd.io/r/c/vpp/+/47513>`_ [VECr 1]: tests: fix mtu test assertions
  | `46527 <https:////gerrit.fd.io/r/c/vpp/+/46527>`_ [VECr 2]: lb: add NAT6_NOPORT encap type
  | `47476 <https:////gerrit.fd.io/r/c/vpp/+/47476>`_ [VECr 2]: mss_clamp: reset interface state on interface delete
  | `47295 <https:////gerrit.fd.io/r/c/vpp/+/47295>`_ [VECr 2]: linux-cp: delete multicast routes from the MFIB
  | `46959 <https:////gerrit.fd.io/r/c/vpp/+/46959>`_ [VECr 2]: linux-cp: free lcp_router_table if 0 routes and no lcp pairs only
  | `47425 <https:////gerrit.fd.io/r/c/vpp/+/47425>`_ [VECr 5]: bfd: add S-BFD reflector datapath
  | `47426 <https:////gerrit.fd.io/r/c/vpp/+/47426>`_ [VECr 5]: bfd: reflect S-BFD requests sent over MPLS paths
  | `47423 <https:////gerrit.fd.io/r/c/vpp/+/47423>`_ [VECr 5]: bfd: add S-BFD reflector configuration
  | `46720 <https:////gerrit.fd.io/r/c/vpp/+/46720>`_ [VECr 5]: tests: make qemu network lock recoverable
  | `47335 <https:////gerrit.fd.io/r/c/vpp/+/47335>`_ [VECr 10]: tests: centralize UDP packet info decoding
  | `46907 <https:////gerrit.fd.io/r/c/vpp/+/46907>`_ [VECr 10]: fastacl: RFC 8955 FlowSpec filter for volumetric DDoS mitigation
  | `46728 <https:////gerrit.fd.io/r/c/vpp/+/46728>`_ [VECr 11]: ipsec: IPTFS (RFC 9347) unit tests
  | `47273 <https:////gerrit.fd.io/r/c/vpp/+/47273>`_ [VECr 12]: ip-neighbor: add neighbour table event counters
  | `47217 <https:////gerrit.fd.io/r/c/vpp/+/47217>`_ [VECr 12]: mss_clamp: fix IPv4 vector MSS interface
  | `47279 <https:////gerrit.fd.io/r/c/vpp/+/47279>`_ [VECr 13]: linux-cp: flush IPv4 routes whenever the host link goes down
  | `47120 <https:////gerrit.fd.io/r/c/vpp/+/47120>`_ [VECr 13]: linux-cp: do not unlock an mfib for MPLS tables
  | `47192 <https:////gerrit.fd.io/r/c/vpp/+/47192>`_ [VECr 13]: ikev2: keep GRE protection on Child Delete
  | `47276 <https:////gerrit.fd.io/r/c/vpp/+/47276>`_ [VECr 13]: arp: fix reply for local address with adj-fib
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 13]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `46991 <https:////gerrit.fd.io/r/c/vpp/+/46991>`_ [VECr 13]: pppoeclient: echo relay tag and accept PADS without AC-Cookie
  | `47264 <https:////gerrit.fd.io/r/c/vpp/+/47264>`_ [VECr 15]: l2: refuse L3-only bridge and xconnect members
  | `47263 <https:////gerrit.fd.io/r/c/vpp/+/47263>`_ [VECr 15]: span gre: refuse destinations with no output node
  | `47242 <https:////gerrit.fd.io/r/c/vpp/+/47242>`_ [VECr 15]: ikev2: accept responder-initiated Child SA rekey
  | `47194 <https:////gerrit.fd.io/r/c/vpp/+/47194>`_ [VECr 15]: ikev2: allocate Child SA IDs without collision
  | `47247 <https:////gerrit.fd.io/r/c/vpp/+/47247>`_ [VECr 15]: ikev2: accept additional Child SA from responder
  | `47222 <https:////gerrit.fd.io/r/c/vpp/+/47222>`_ [VECr 15]: linux-cp: avoid a drop path on first route source
  | `47241 <https:////gerrit.fd.io/r/c/vpp/+/47241>`_ [VECr 15]: ikev2: preserve responses across local requests
  | `47252 <https:////gerrit.fd.io/r/c/vpp/+/47252>`_ [VECr 16]: nat: select dynamic translation by source prefix
  | `46963 <https:////gerrit.fd.io/r/c/vpp/+/46963>`_ [VECr 18]: tests: fix fragment_rfc791/fragment_rfc8200 bugs
  | `47214 <https:////gerrit.fd.io/r/c/vpp/+/47214>`_ [VECr 19]: ikev2: configure inbound ESP replay window
  | `47076 <https:////gerrit.fd.io/r/c/vpp/+/47076>`_ [VECr 23]: fib: decide the glean source by the address it holds
  | `47078 <https:////gerrit.fd.io/r/c/vpp/+/47078>`_ [VECr 25]: fib: swap in the paths of a source new to the entry
  | `47020 <https:////gerrit.fd.io/r/c/vpp/+/47020>`_ [VECr 30]: tests: skip parameterized_class base classes in discovery

udp: **Florin Coras** <fcoras@cisco.com>
  | `47424 <https:////gerrit.fd.io/r/c/vpp/+/47424>`_ [VECr 5]: udp: add S-BFD port 7784 to the UDP port lists
  | `46284 <https:////gerrit.fd.io/r/c/vpp/+/46284>`_ [VECr 16]: udp: add segmentation offload support

unittest: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `47450 <https:////gerrit.fd.io/r/c/vpp/+/47450>`_ [VECr 3]: rdma: add cloned TX packet probe
  | `47402 <https:////gerrit.fd.io/r/c/vpp/+/47402>`_ [VECr 6]: fib: fix stale importer pointer in attached-export walk
  | `46461 <https:////gerrit.fd.io/r/c/vpp/+/46461>`_ [VECr 12]: ipsec: IPTFS (RFC 9347)
  | `47078 <https:////gerrit.fd.io/r/c/vpp/+/47078>`_ [VECr 25]: fib: swap in the paths of a source new to the entry

vat2: **Ole Troan** <otroan@employees.org>
  | `47510 <https:////gerrit.fd.io/r/c/vpp/+/47510>`_ [VECr 1]: vat2: bound and fail-closed the JSON file read

vcl: **Florin Coras** <fcoras@cisco.com>
  | `45941 <https:////gerrit.fd.io/r/c/vpp/+/45941>`_ [VECr 1]: misc: patch to test CI infra

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `47205 <https:////gerrit.fd.io/r/c/vpp/+/47205>`_ [VECr 13]: vlib: avoid null pointer arithmetic in main walk
  | `47255 <https:////gerrit.fd.io/r/c/vpp/+/47255>`_ [VECr 15]: vlib: preserve const in plugin suffix lookup

vperf: **Florin Coras** <fcoras@cisco.com>, **Matus Fabian** <matfabia@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `47343 <https:////gerrit.fd.io/r/c/vpp/+/47343>`_ [VECr 0]: session: fix certificate registration race

vpp: **Dave Barach** <vpp@barachs.net>
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 13]: pppoeclient: add PPPoE client plugin with DHCPv6 observability

vppapigen: **Ole Troan** <otroan@employees.org>
  | `47253 <https:////gerrit.fd.io/r/c/vpp/+/47253>`_ [VECr 16]: vppapigen: support output plugins on Python 3.15
  | `44551 <https:////gerrit.fd.io/r/c/vpp/+/44551>`_ [VECr 25]: vppapigen: fix inconsistency in paths JSON

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `47519 <https:////gerrit.fd.io/r/c/vpp/+/47519>`_ [VECr 1]: vppinfra: free key_tmps in mhash_free
  | `45470 <https:////gerrit.fd.io/r/c/vpp/+/45470>`_ [VECr 11]: vppinfra: add cast to prevent warning
  | `47204 <https:////gerrit.fd.io/r/c/vpp/+/47204>`_ [VECr 13]: vppinfra: avoid null member access on hash miss
  | `47188 <https:////gerrit.fd.io/r/c/vpp/+/47188>`_ [VECr 13]: vppinfra: use unsigned CPU feature masks

vxlan: **John Lo** <lojultra2020@outlook.com>, **Steven Luong** <sluong@cisco.com>
  | `47322 <https:////gerrit.fd.io/r/c/vpp/+/47322>`_ [VECr 10]: vxlan: check available headroom

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Akeel Ali** <akeelapi@gmail.com>:

  | `45686 <https:////gerrit.fd.io/r/c/vpp/+/45686>`_ [Vec 146]: ip_validate: new plugin to drop packets with invalid addresses

**Akos Orban** <orbanakos2001@gmail.com>:

  | `44995 <https:////gerrit.fd.io/r/c/vpp/+/44995>`_ [VEc 5]: cnat: fix show cnat client showing invalid for client id
  | `45001 <https:////gerrit.fd.io/r/c/vpp/+/45001>`_ [vEC 6]: cnat: fix show cnat translation for specific translation id

**Alexander Chernavin** <chernavin@mts.ru>:

  | `46481 <https:////gerrit.fd.io/r/c/vpp/+/46481>`_ [VeC 61]: acl: add callback hooks for list add/del
  | `43726 <https:////gerrit.fd.io/r/c/vpp/+/43726>`_ [vec 69]: vhost: fix rxvq interrupts triggered because of race

**Alexander Skorichenko** <askorichenko@netgate.com>:

  | `45877 <https:////gerrit.fd.io/r/c/vpp/+/45877>`_ [VeC 170]: snort: don't store snort metadata in buffer

**Andrey Vasilevsky** <anvanster@gmail.com>:

  | `46487 <https:////gerrit.fd.io/r/c/vpp/+/46487>`_ [VeC 38]: nat: look up address-only static mappings with protocol 0

**Anil Kainikara** <anilkumar911@gmail.com>:

  | `46256 <https:////gerrit.fd.io/r/c/vpp/+/46256>`_ [vec 115]: crypto: openssl - check ctx alloc/init in key-add

**Anton Blazhko** <ablazhko@cisco.com>:

  | `45808 <https:////gerrit.fd.io/r/c/vpp/+/45808>`_ [Vec 32]: devices: Convert PIPE to plugin

**Aritra Basu** <aritrbas@cisco.com>:

  | `47291 <https:////gerrit.fd.io/r/c/vpp/+/47291>`_ [VEc 0]: tests: set core_pattern in CI
  | `45074 <https:////gerrit.fd.io/r/c/vpp/+/45074>`_ [veC 45]: ip6-nd: enforce on-link source validation for ND learning
  | `46593 <https:////gerrit.fd.io/r/c/vpp/+/46593>`_ [VeC 68]: tests: bypass http/https proxy in test curl invocations
  | `46530 <https:////gerrit.fd.io/r/c/vpp/+/46530>`_ [VeC 81]: gha: skip build/test verify jobs for docs-only changes
  | `45705 <https:////gerrit.fd.io/r/c/vpp/+/45705>`_ [Vec 124]: kube-test: support CalicoVPP repo restructure (backward-compatible)
  | `46048 <https:////gerrit.fd.io/r/c/vpp/+/46048>`_ [VeC 131]: tcp: add TCP fast open support (RFC 7413)
  | `46167 <https:////gerrit.fd.io/r/c/vpp/+/46167>`_ [veC 135]: kube-test: retry Job finalizer cleanup conflicts
  | `45583 <https:////gerrit.fd.io/r/c/vpp/+/45583>`_ [VeC 149]: vlib: fix trace flag loss when multiple pending frames share next frame

**Benoît Ganne** <bganne@cisco.com>:

  | `46368 <https:////gerrit.fd.io/r/c/vpp/+/46368>`_ [VeC 103]: vppinfra: make vec_foreach_pointer empty-safe
  | `46117 <https:////gerrit.fd.io/r/c/vpp/+/46117>`_ [VeC 139]: vppapigen: fix vppapigen depfile without imports
  | `46087 <https:////gerrit.fd.io/r/c/vpp/+/46087>`_ [VeC 139]: cnat: wait for cnat scanner session cleanup

**Damjan Marion** <dmarion@0xa5.net>:

  | `47551 <https:////gerrit.fd.io/r/c/vpp/+/47551>`_ [vEC 0]: atlantic: fix lso tx path initialization
  | `47543 <https:////gerrit.fd.io/r/c/vpp/+/47543>`_ [vEC 0]: ige: receive multicast frames
  | `47542 <https:////gerrit.fd.io/r/c/vpp/+/47542>`_ [vEC 0]: ige: count rx buffer allocation failures
  | `45409 <https:////gerrit.fd.io/r/c/vpp/+/45409>`_ [veC 156]: ikev2: add Curve25519 and Curve448 DH groups

**Dennis Lanov** <dennis.lanov@gmail.com>:

  | `46270 <https:////gerrit.fd.io/r/c/vpp/+/46270>`_ [VeC 116]: acl: correct interface command help

**Florin Coras** <florin.coras@gmail.com>:

  | `47527 <https:////gerrit.fd.io/r/c/vpp/+/47527>`_ [vEC 0]: session: check fifo alloc thread on dealloc
  | `47528 <https:////gerrit.fd.io/r/c/vpp/+/47528>`_ [vEC 0]: hsi: fix handling of fifos taken over from apps
  | `46687 <https:////gerrit.fd.io/r/c/vpp/+/46687>`_ [veC 68]: vppinfra: avoid duplicate rbtree custom comparison

**G. Paul Ziemba** <pz-vpp-dev@ziemba.us>:

  | `45510 <https:////gerrit.fd.io/r/c/vpp/+/45510>`_ [veC 64]: crypto: add op tracing capability
  | `45699 <https:////gerrit.fd.io/r/c/vpp/+/45699>`_ [VeC 93]: dpdk: buffer bug fixes

**Gopalakrishnan Subramani** <gsubramani@idirect.net>:

  | `47023 <https:////gerrit.fd.io/r/c/vpp/+/47023>`_ [vEC 30]: igmp: set proxy mfib Accept on host and Forward on router

**GregMiller** <greg@gregmiller.co.za>:

  | `46129 <https:////gerrit.fd.io/r/c/vpp/+/46129>`_ [VeC 138]: pppoe: native per-session rx policing in pppoe-decap node
  | `46125 <https:////gerrit.fd.io/r/c/vpp/+/46125>`_ [VeC 138]: pppoe: add combined subscriber session provisioning API

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [Vec 33]: sfdp: add sfdp-session-stats service
  | `46588 <https:////gerrit.fd.io/r/c/vpp/+/46588>`_ [veC 69]: sfdp_services: various sfdp nat improvements
  | `44847 <https:////gerrit.fd.io/r/c/vpp/+/44847>`_ [VeC 130]: sfdp: modify tenant_index type from u16 to u32
  | `45964 <https:////gerrit.fd.io/r/c/vpp/+/45964>`_ [VeC 137]: flow: add parameter to pre-allocate global pool
  | `45481 <https:////gerrit.fd.io/r/c/vpp/+/45481>`_ [veC 137]: flow: add action VNET_FLOW_ACTION_STEER_TO_PORT
  | `45637 <https:////gerrit.fd.io/r/c/vpp/+/45637>`_ [VeC 137]: dpdk: add support for VNET_FLOW_ACTION_AGE action
  | `45633 <https:////gerrit.fd.io/r/c/vpp/+/45633>`_ [veC 137]: dpdk: add support for represented port action
  | `45482 <https:////gerrit.fd.io/r/c/vpp/+/45482>`_ [Vec 138]: sfdp: add verdict-testbench service
  | `46043 <https:////gerrit.fd.io/r/c/vpp/+/46043>`_ [VeC 138]: flow: add APIs to support new flow actions
  | `45636 <https:////gerrit.fd.io/r/c/vpp/+/45636>`_ [VeC 138]: flow: add flow aging support
  | `45635 <https:////gerrit.fd.io/r/c/vpp/+/45635>`_ [VeC 150]: dpdk: add support for VNET_FLOW_ACTION_COUNT
  | `45634 <https:////gerrit.fd.io/r/c/vpp/+/45634>`_ [VeC 150]: flow: implement VNET_FLOW_ACTION_COUNT operation
  | `45938 <https:////gerrit.fd.io/r/c/vpp/+/45938>`_ [Vec 153]: tracepath: minor refactoring to code
  | `45848 <https:////gerrit.fd.io/r/c/vpp/+/45848>`_ [VeC 174]: sfdp: fix specification of scope_index

**Hanataba Azaka** <northern.snow.x@gmail.com>:

  | `46041 <https:////gerrit.fd.io/r/c/vpp/+/46041>`_ [VEc 9]: cnat: make session scanner budget configurable

**Hedi Bouattour** <hedibouattour2010@gmail.com>:

  | `46147 <https:////gerrit.fd.io/r/c/vpp/+/46147>`_ [Vec 135]: npol: support prednat policies
  | `45914 <https:////gerrit.fd.io/r/c/vpp/+/45914>`_ [Vec 139]: cnat: preallocate ts_pools to eliminate reader locks on timestamp get

**Ivan Ivanets** <iivanets@cisco.com>:

  | `46955 <https:////gerrit.fd.io/r/c/vpp/+/46955>`_ [VEc 3]: ip6: fix Pad1 off-by-one in hop-by-hop option pars

**Ivan Shvedunov** <ishvedunov@netgate.com>:

  | `47116 <https:////gerrit.fd.io/r/c/vpp/+/47116>`_ [vEC 23]: fib: populate the glean on source reactivation
  | `46905 <https:////gerrit.fd.io/r/c/vpp/+/46905>`_ [VeC 41]: vapi: mark unregistered vl_msg_ids invalid in the lookup table

**Janik** <janik.haag@imc.com>:

  | `46122 <https:////gerrit.fd.io/r/c/vpp/+/46122>`_ [Vec 110]: build: fix make install-deps for fedora targets
  | `46123 <https:////gerrit.fd.io/r/c/vpp/+/46123>`_ [VeC 139]: vcl: add regression test for nonblocking connect()
  | `46124 <https:////gerrit.fd.io/r/c/vpp/+/46124>`_ [VeC 139]: vcl: add regression test for ignorable flags
  | `46121 <https:////gerrit.fd.io/r/c/vpp/+/46121>`_ [VeC 139]: sasc: fix gcc uninitialized warning

**Jerome Tollet** <jtollet@cisco.com>:

  | `46808 <https:////gerrit.fd.io/r/c/vpp/+/46808>`_ [VeC 34]: docs: announce libvnet visibility change

**Jianquan Ye** <jianquanye@microsoft.com>:

  | `45864 <https:////gerrit.fd.io/r/c/vpp/+/45864>`_ [Vec 151]: ip bonding hash: inner-aware flow hash (opt-in)

**Kai Ji** <kai.ji@intel.com>:

  | `46925 <https:////gerrit.fd.io/r/c/vpp/+/46925>`_ [VEc 11]: crypto: fix engine registration and async dispatch
  | `46926 <https:////gerrit.fd.io/r/c/vpp/+/46926>`_ [VeC 34]: dpdk: fix QAT cryptodev AEAD sessions
  | `46927 <https:////gerrit.fd.io/r/c/vpp/+/46927>`_ [VeC 39]: crypto: fix fixed-tag AEAD validation

**Keith Spinney** <kspinney@cisco.com>:

  | `46525 <https:////gerrit.fd.io/r/c/vpp/+/46525>`_ [Vec 34]: fib: barrier-protect fib_path_list_destroy()

**Klement Sekera** <ksekera@netgate.com>:

  | `46789 <https:////gerrit.fd.io/r/c/vpp/+/46789>`_ [vEC 30]: test: wait for handoff queues to drain before reading a capture
  | `46995 <https:////gerrit.fd.io/r/c/vpp/+/46995>`_ [VeC 31]: tests: improve return type consistency
  | `46788 <https:////gerrit.fd.io/r/c/vpp/+/46788>`_ [VeC 55]: vlib: add show handoff pending CLI
  | `46013 <https:////gerrit.fd.io/r/c/vpp/+/46013>`_ [VeC 118]: build: include GNUInstallDirs in VPPConfig
  | `45728 <https:////gerrit.fd.io/r/c/vpp/+/45728>`_ [VeC 118]: api: add build-time python stub generation via vppapigen

**Longxiang Lyu** <lolv@microsoft.com>:

  | `45685 <https:////gerrit.fd.io/r/c/vpp/+/45685>`_ [Vec 150]: ipip: add p2ap ipip tunnel
  | `45898 <https:////gerrit.fd.io/r/c/vpp/+/45898>`_ [Vec 151]: ip: add 'no-class-e-drop' startup config option to suppress class E drop route

**Matus Fabian** <mfabianlf@pm.me>:

  | `46579 <https:////gerrit.fd.io/r/c/vpp/+/46579>`_ [vEC 0]: misc: patch to test maketest action timeout
  | `46262 <https:////gerrit.fd.io/r/c/vpp/+/46262>`_ [VeC 34]: iavf: add setup documentation

**Maxime Peim** <maxime.peim@gmail.com>:

  | `45254 <https:////gerrit.fd.io/r/c/vpp/+/45254>`_ [VEc 2]: policer: prevent deletion of referenced policers
  | `45098 <https:////gerrit.fd.io/r/c/vpp/+/45098>`_ [vEc 2]: dpdk: support async flow offload
  | `46032 <https:////gerrit.fd.io/r/c/vpp/+/46032>`_ [veC 151]: docs: document build-time VPP parameters
  | `45152 <https:////gerrit.fd.io/r/c/vpp/+/45152>`_ [VeC 157]: dpdk: install default jump-to-group-1 rule for mlx5
  | `45539 <https:////gerrit.fd.io/r/c/vpp/+/45539>`_ [veC 157]: dpdk: multi-thread async flow offload with per-worker caches

**Micha? Czerwonka** <mczka.mczka@gmail.com>:

  | `46900 <https:////gerrit.fd.io/r/c/vpp/+/46900>`_ [VeC 38]: vpp: vpp/vnet/main.c fix parsing vpp option and improve description of usage

**Mohammad Mahdi Nemati Haravani** <nemati.mahdi255@gmail.com>:

  | `44303 <https:////gerrit.fd.io/r/c/vpp/+/44303>`_ [VEc 4]: build: fix vpp-ext-deps install and clean paths

**Mohammed HAWARI** <momohawari@gmail.com>:

  | `42343 <https:////gerrit.fd.io/r/c/vpp/+/42343>`_ [VeC 79]: vcl: LDP default to regular option

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `42886 <https:////gerrit.fd.io/r/c/vpp/+/42886>`_ [Vec 83]: ipip: fix support for ipip6o6 from linux tunnel

**Mykyta Demusenko** <mdemusen@cisco.com>:

  | `46625 <https:////gerrit.fd.io/r/c/vpp/+/46625>`_ [VeC 60]: teib: move the TEIB implementation to a plugin
  | `46602 <https:////gerrit.fd.io/r/c/vpp/+/46602>`_ [Vec 60]: teib: narrow the C API and add a vnet-owned service boundary
  | `46724 <https:////gerrit.fd.io/r/c/vpp/+/46724>`_ [Vec 60]: teib: add tests for the TEIB API

**Nicolas PLANEL** <nplanel@gmail.com>:

  | `44976 <https:////gerrit.fd.io/r/c/vpp/+/44976>`_ [vec 157]: sfdp: async offload lookup

**Ole Troan** <otroan@employees.org>:

  | `46920 <https:////gerrit.fd.io/r/c/vpp/+/46920>`_ [VEc 3]: ip: stop forwarding the Ethernet trailer
  | `46982 <https:////gerrit.fd.io/r/c/vpp/+/46982>`_ [veC 34]: papi: read stats scalars and gauges when they are accessed
  | `46511 <https:////gerrit.fd.io/r/c/vpp/+/46511>`_ [veC 66]: stats: add directory command to vpp_get_stats
  | `46434 <https:////gerrit.fd.io/r/c/vpp/+/46434>`_ [VeC 93]: vlib: fix log2 histogram overflow bin writing past the bin vector
  | `46380 <https:////gerrit.fd.io/r/c/vpp/+/46380>`_ [Vec 100]: vppapigen: fix unaligned access to packed messages

**Onong Tayeng** <onong.tayeng@gmail.com>:

  | `46753 <https:////gerrit.fd.io/r/c/vpp/+/46753>`_ [VEc 5]: cnat: prevent SNAT policy aliasing across FIBs
  | `46726 <https:////gerrit.fd.io/r/c/vpp/+/46726>`_ [Vec 46]: cnat: clear stale default SNAT policy pointer
  | `46752 <https:////gerrit.fd.io/r/c/vpp/+/46752>`_ [Vec 54]: cnat: update cnat plugin documentation
  | `46471 <https:////gerrit.fd.io/r/c/vpp/+/46471>`_ [Vec 58]: cnat: improve flow statistics and error coverage

**Paul Vinciguerra** <pvinci@vinciconsulting.com>:

  | `47190 <https:////gerrit.fd.io/r/c/vpp/+/47190>`_ [VEc 16]: af_packet: preserve VLAN TPID when restoring stripped tags

**Pavel Lavrukhin** <danttevip@gmail.com>:

  | `47516 <https:////gerrit.fd.io/r/c/vpp/+/47516>`_ [VEc 1]: session: clean up rx mqs on eventfd failure
  | `47339 <https:////gerrit.fd.io/r/c/vpp/+/47339>`_ [VEc 1]: ikev2: fetch cipher/MD once in crypto_init
  | `47112 <https:////gerrit.fd.io/r/c/vpp/+/47112>`_ [VEc 1]: ikev2 ipip: negotiate USE_TRANSPORT_MODE
  | `47193 <https:////gerrit.fd.io/r/c/vpp/+/47193>`_ [VEc 1]: ikev2: preserve SA IDs after vector shift

**Pavlo Piatakov** <ppiatako@cisco.com>:

  | `46760 <https:////gerrit.fd.io/r/c/vpp/+/46760>`_ [VeC 60]: cnat: do not count unsupported IP protocols as session alloc failure

**Pawel Szymanski** <pawel.szymanski@intel.com>:

  | `47056 <https:////gerrit.fd.io/r/c/vpp/+/47056>`_ [VEc 4]: build: Changes in makefiles to enabe build on FreeBSD

**Peter Morrow** <pdmorrow@gmail.com>:

  | `46954 <https:////gerrit.fd.io/r/c/vpp/+/46954>`_ [VEc 27]: vlib: leave a MANA VF down when taking its netvsc device

**Pierre Pfister** <pierre@meter.com>:

  | `46858 <https:////gerrit.fd.io/r/c/vpp/+/46858>`_ [VEc 27]: vlib: resume a process once per suspension

**Poornima Kandhade** <poornika@cisco.com>:

  | `46424 <https:////gerrit.fd.io/r/c/vpp/+/46424>`_ [vEC 19]: sfdp: add lifecycle records to session stats ring

**Qi Zhang** <zzqqqqwq77@gmail.com>:

  | `46458 <https:////gerrit.fd.io/r/c/vpp/+/46458>`_ [veC 70]: vlib: detect freed buffer‑chain on node dispatch for double‑free debug
  | `46643 <https:////gerrit.fd.io/r/c/vpp/+/46643>`_ [veC 71]: vnet: fix double-free in bcast fragment reassembly

**Rakesh Kudurumalla** <rkudurumalla@marvell.com>:

  | `45796 <https:////gerrit.fd.io/r/c/vpp/+/45796>`_ [Vec 165]: pfc: add framework for priority flow control
  | `45797 <https:////gerrit.fd.io/r/c/vpp/+/45797>`_ [VeC 177]: octeon: add PFC support

**Ram Subramanian** <ram@meter.com>:

  | `46442 <https:////gerrit.fd.io/r/c/vpp/+/46442>`_ [VeC 44]: vnet: install missing vnet headers

**Robert Shearman** <robertshearman@gmail.com>:

  | `45957 <https:////gerrit.fd.io/r/c/vpp/+/45957>`_ [VEc 0]: vlib: ASAN-poison unallocated buffers
  | `46050 <https:////gerrit.fd.io/r/c/vpp/+/46050>`_ [VeC 47]: ip: fix ip mroute bulk insertion CLI for certain inputs
  | `46019 <https:////gerrit.fd.io/r/c/vpp/+/46019>`_ [vec 105]: misc: fix potential OOB read during flow hash calculations

**Samuel Benko** <sbenko@cisco.com>:

  | `45765 <https:////gerrit.fd.io/r/c/vpp/+/45765>`_ [VeC 137]: tls: propagate verify config for dtls

**Sergiy Bachynskyy** <sbachyns@cisco.com>:

  | `46206 <https:////gerrit.fd.io/r/c/vpp/+/46206>`_ [VeC 123]: ipfix: move to a plugin

**Shuzo Ichiyoshi** <deadcafe.beef@gmail.com>:

  | `46180 <https:////gerrit.fd.io/r/c/vpp/+/46180>`_ [VeC 96]: session: check event collector lookups
  | `46355 <https:////gerrit.fd.io/r/c/vpp/+/46355>`_ [VeC 103]: ip: fix fragmentation with negative buffer offset
  | `46178 <https:////gerrit.fd.io/r/c/vpp/+/46178>`_ [VeC 103]: session: validate app for async connect RPC
  | `46352 <https:////gerrit.fd.io/r/c/vpp/+/46352>`_ [VeC 105]: vppinfra: serialize VM map page size lookup
  | `46341 <https:////gerrit.fd.io/r/c/vpp/+/46341>`_ [VeC 107]: hsa: make TLS client CLI MP-safe
  | `46311 <https:////gerrit.fd.io/r/c/vpp/+/46311>`_ [VeC 109]: tcp: handle retransmitted SYN-ACK in TIME-WAIT

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `44249 <https:////gerrit.fd.io/r/c/vpp/+/44249>`_ [VEc 9]: fib: dump by src not only contributing routes
  | `47106 <https:////gerrit.fd.io/r/c/vpp/+/47106>`_ [VEc 10]: vnet: rewrite nodes to check available headroom

**Suresh Sundararaman** <suresh.serc@gmail.com>:

  | `46516 <https:////gerrit.fd.io/r/c/vpp/+/46516>`_ [vEC 3]: misc: surs patch to test CI infra
  | `47289 <https:////gerrit.fd.io/r/c/vpp/+/47289>`_ [vEC 12]: tests: add temporary core backtrace crash diagnostic
  | `46529 <https:////gerrit.fd.io/r/c/vpp/+/46529>`_ [VeC 80]: docs: Get the VPP Source

**Viacheslav Zakharchenko** <vzakharc@cisco.com>:

  | `45807 <https:////gerrit.fd.io/r/c/vpp/+/45807>`_ [Vec 116]: bfd: Introduce vppinfra/callback_data based vnet notifier for FIB/ADJ notifications
  | `45810 <https:////gerrit.fd.io/r/c/vpp/+/45810>`_ [Vec 117]: bfd: Extract to plugin

**Vladimir Lavor** <vlavor@cisco.com>:

  | `46268 <https:////gerrit.fd.io/r/c/vpp/+/46268>`_ [VeC 116]: vlib: expose error severity in stats segment

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `45650 <https:////gerrit.fd.io/r/c/vpp/+/45650>`_ [Vec 174]: flowprobe: count based sampling support

**Vratko Polak** <vrpolak@cisco.com>:

  | `46703 <https:////gerrit.fd.io/r/c/vpp/+/46703>`_ [VeC 51]: buffers: make natural layout always default
  | `45047 <https:////gerrit.fd.io/r/c/vpp/+/45047>`_ [vec 163]: sfdp_services: add basic support for time-wait

**Wei Wang** <weiwa@cisco.com>:

  | `46085 <https:////gerrit.fd.io/r/c/vpp/+/46085>`_ [Vec 136]: tls: tls session resumption code and host stack tests

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `45901 <https:////gerrit.fd.io/r/c/vpp/+/45901>`_ [VeC 165]: vppinfra: fix use-after-poison issue in vec_foreach_pointer and pool_foreach_pointer
  | `45902 <https:////gerrit.fd.io/r/c/vpp/+/45902>`_ [Vec 165]: vppinfra: fix ASAN issue vec_len not thread safe
  | `45894 <https:////gerrit.fd.io/r/c/vpp/+/45894>`_ [veC 166]: vlib: vlib_node_rename should be guarded by thread barrier
  | `45895 <https:////gerrit.fd.io/r/c/vpp/+/45895>`_ [VeC 167]: vlib: fix process state format output wrapped by extra quotes
  | `45860 <https:////gerrit.fd.io/r/c/vpp/+/45860>`_ [vec 172]: vlib: pre-input node should be dispatched before input node

**Yang Liu** <numbksco@gmail.com>:

  | `46018 <https:////gerrit.fd.io/r/c/vpp/+/46018>`_ [Vec 128]: vppinfra: add loongarch64 architecture support

**Yuto Suzuki** <offside.items03@icloud.com>:

  | `45503 <https:////gerrit.fd.io/r/c/vpp/+/45503>`_ [Vec 40]: ip6-nd: update secondary RA prefixes for subnets
  | `45504 <https:////gerrit.fd.io/r/c/vpp/+/45504>`_ [Vec 40]: ip6-nd: support RDNSS option in IPv6 RA

**marek zavodsky** <mazavods@gmail.com>:

  | `47316 <https:////gerrit.fd.io/r/c/vpp/+/47316>`_ [VEc 2]: http: h1 - handling of big request/response header section

**niklesh** <nikleshparshaboina@gmail.com>:

  | `45016 <https:////gerrit.fd.io/r/c/vpp/+/45016>`_ [veC 34]: cnat: add scope_id to session key
  | `46546 <https:////gerrit.fd.io/r/c/vpp/+/46546>`_ [VeC 77]: vlib: re-base the timing wheel when arming an empty wheel

**steven luong** <sluong@cisco.com>:

  | `45756 <https:////gerrit.fd.io/r/c/vpp/+/45756>`_ [VEc 18]: vcl: fix crash when closing listener with pending accepts
  | `45838 <https:////gerrit.fd.io/r/c/vpp/+/45838>`_ [VeC 178]: tls: add ALPN negotiation support

Abandoned:
----------
**The following gerrit changes have not been updated in over 180 days and have been abandoned.**

**steven luong** <sluong@cisco.com>:

  | `45816 <https:////gerrit.fd.io/r/c/vpp/+/45816>`_ [A 180]: tls: fix picotls partial record handling

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
authors          145
maintainers      119
committers       1
abandoned        1
================ ===

