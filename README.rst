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
generated on Friday 2026-11-27, 09:38:15
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

  | `48260 <https:////gerrit.fd.io/r/c/vpp/+/48260>`_ [VECR 0]: tests: reuse ipv4 fib dumps for route assertions
  | `48263 <https:////gerrit.fd.io/r/c/vpp/+/48263>`_ [VECR 0]: tests: speed up uncolored packet hexdumps
  | `48261 <https:////gerrit.fd.io/r/c/vpp/+/48261>`_ [VECR 0]: tests: limit ci packet log expansion to failures
  | `48245 <https:////gerrit.fd.io/r/c/vpp/+/48245>`_ [VECR 0]: tests: avoid timed captures in synchronous esp
  | `48212 <https:////gerrit.fd.io/r/c/vpp/+/48212>`_ [VECR 0]: tests: check malformed ipv6 fragment rejection

Maintainers:
------------
| **Please review these gerrit changes.**

| **NOTE: Gerrit changes may be included under more than one feature based on the modified files regardless of the feature list included on the commit headline.**

abf: **Neale Ranns** <neale@graphiant.com>
  | `48209 <https:////gerrit.fd.io/r/c/vpp/+/48209>`_ [VECr 1]: abf: clear stale flow hash left by reassembly

acl: **Andrew Yourtchenko** <ayourtch@gmail.com>
  | `47511 <https:////gerrit.fd.io/r/c/vpp/+/47511>`_ [VECr 0]: acl: bound collision-list rescans on no-op split
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader

adl: **Dave Barach** <vpp@barachs.net>
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader

af_packet: **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader
  | `47707 <https:////gerrit.fd.io/r/c/vpp/+/47707>`_ [VECr 10]: af_packet: set ip4 checksum offload flag
  | `47190 <https:////gerrit.fd.io/r/c/vpp/+/47190>`_ [VECr 12]: af_packet: preserve VLAN TPID when restoring stripped tags
  | `47623 <https:////gerrit.fd.io/r/c/vpp/+/47623>`_ [VECr 16]: af_packet: fix polling queue count on new queues
  | `47515 <https:////gerrit.fd.io/r/c/vpp/+/47515>`_ [VECr 19]: af_packet: restore 802.1ad tags with the correct TPID

af_xdp: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `48222 <https:////gerrit.fd.io/r/c/vpp/+/48222>`_ [VECr 0]: af_xdp: convert cli commands
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader

api: **Dave Barach** <vpp@barachs.net>
  | `48255 <https:////gerrit.fd.io/r/c/vpp/+/48255>`_ [VECr 0]: vlib: write the memory trace JSON with clib_json
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader
  | `48046 <https:////gerrit.fd.io/r/c/vpp/+/48046>`_ [VECr 4]: api: convert the api CLI commands to the declarative CLI
  | `47909 <https:////gerrit.fd.io/r/c/vpp/+/47909>`_ [VECr 8]: api: Modify shared memory handling to support FreeBSD
  | `47635 <https:////gerrit.fd.io/r/c/vpp/+/47635>`_ [VECr 16]: vapi: Incorrect handling EAGAIN on unix domain socket transport

arp: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader

arping: **Steven Luong** <sluong@cisco.com>
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader

bfd: **Klement Sekera** <klement.sekera@gmail.com>
  | `48230 <https:////gerrit.fd.io/r/c/vpp/+/48230>`_ [VECr 0]: bfd: convert cli commands
  | `47427 <https:////gerrit.fd.io/r/c/vpp/+/47427>`_ [VECr 4]: bfd: document the S-BFD reflector
  | `47425 <https:////gerrit.fd.io/r/c/vpp/+/47425>`_ [VECr 4]: bfd: add S-BFD reflector datapath
  | `47423 <https:////gerrit.fd.io/r/c/vpp/+/47423>`_ [VECr 4]: bfd: add S-BFD reflector configuration
  | `47426 <https:////gerrit.fd.io/r/c/vpp/+/47426>`_ [VECr 4]: bfd: reflect S-BFD requests sent over MPLS paths

buffers: **Damjan Marion** <damarion@cisco.com>, **Dave Barach** <vpp@barachs.net>
  | `47321 <https:////gerrit.fd.io/r/c/vpp/+/47321>`_ [VECr 17]: vlib: add helper to check available headroom in vlib_buffer_t

build: **Damjan Marion** <damarion@cisco.com>
  | `48266 <https:////gerrit.fd.io/r/c/vpp/+/48266>`_ [VECr 0]: build: don't use pack-relative-relocs where ld ignores it
  | `48202 <https:////gerrit.fd.io/r/c/vpp/+/48202>`_ [VECr 0]: build: fetch matching ext deps in fdio ci
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader
  | `46907 <https:////gerrit.fd.io/r/c/vpp/+/46907>`_ [VECr 8]: fastacl: RFC 8955 FlowSpec filter for volumetric DDoS mitigation
  | `47056 <https:////gerrit.fd.io/r/c/vpp/+/47056>`_ [VECr 14]: build: Changes in makefiles to enabe build on FreeBSD

cdp: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader

crypto: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>
  | `47696 <https:////gerrit.fd.io/r/c/vpp/+/47696>`_ [VECr 15]: crypto: retain contexts until asynchronous work completes

ct6: **Dave Barach** <vpp@barachs.net>
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader

dhcp: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `47514 <https:////gerrit.fd.io/r/c/vpp/+/47514>`_ [VECr 0]: dhcp: bound client option parsing to the packet
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader
  | `47868 <https:////gerrit.fd.io/r/c/vpp/+/47868>`_ [VECr 3]: dhcp: export DHCPv6 runtime state getters

dns: **Dave Barach** <vpp@barachs.net>
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `48259 <https:////gerrit.fd.io/r/c/vpp/+/48259>`_ [VECr 0]: vppinfra: let a CLI value select further arguments
  | `47894 <https:////gerrit.fd.io/r/c/vpp/+/47894>`_ [VECr 0]: sfdp: per-tenant pre-filter for new sessions
  | `45098 <https:////gerrit.fd.io/r/c/vpp/+/45098>`_ [VECr 0]: dpdk: support async flow offload
  | `48213 <https:////gerrit.fd.io/r/c/vpp/+/48213>`_ [VECr 0]: tests: give declarative cli tests a unique name
  | `48056 <https:////gerrit.fd.io/r/c/vpp/+/48056>`_ [VECr 2]: vpp: rewrite the binary-api CLI using the API descriptors
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 3]: pppoeclient: add PPPoE client plugin
  | `47427 <https:////gerrit.fd.io/r/c/vpp/+/47427>`_ [VECr 4]: bfd: document the S-BFD reflector
  | `47423 <https:////gerrit.fd.io/r/c/vpp/+/47423>`_ [VECr 4]: bfd: add S-BFD reflector configuration
  | `46032 <https:////gerrit.fd.io/r/c/vpp/+/46032>`_ [VECr 8]: docs: document build-time VPP parameters
  | `46907 <https:////gerrit.fd.io/r/c/vpp/+/46907>`_ [VECr 8]: fastacl: RFC 8955 FlowSpec filter for volumetric DDoS mitigation
  | `47274 <https:////gerrit.fd.io/r/c/vpp/+/47274>`_ [VECr 8]: freebsd-cp: FreeBSD Control Plane plugin similar to Linux CP plugin but siginificantly simplified
  | `45505 <https:////gerrit.fd.io/r/c/vpp/+/45505>`_ [VECr 8]: rdma: add mlx5 dv tso support for raw packet tx
  | `46527 <https:////gerrit.fd.io/r/c/vpp/+/46527>`_ [VECr 20]: lb: add NAT6_NOPORT encap type
  | `46461 <https:////gerrit.fd.io/r/c/vpp/+/46461>`_ [VECr 30]: ipsec: IPTFS (RFC 9347)

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `48223 <https:////gerrit.fd.io/r/c/vpp/+/48223>`_ [VECr 0]: dpdk: convert cli commands
  | `45098 <https:////gerrit.fd.io/r/c/vpp/+/45098>`_ [VECr 0]: dpdk: support async flow offload
  | `46939 <https:////gerrit.fd.io/r/c/vpp/+/46939>`_ [VECr 1]: dpdk: don't leak chained mbufs when multi-seg is disabled
  | `47056 <https:////gerrit.fd.io/r/c/vpp/+/47056>`_ [VECr 14]: build: Changes in makefiles to enabe build on FreeBSD
  | `45675 <https:////gerrit.fd.io/r/c/vpp/+/45675>`_ [VECr 16]: dpdk: log MFIB MAC replay tolerance at debug level
  | `47480 <https:////gerrit.fd.io/r/c/vpp/+/47480>`_ [VECr 20]: dpdk: fix alignment of rx and tx trace records

ebuild: **Dave Barach** <vpp@barachs.net>
  | `47056 <https:////gerrit.fd.io/r/c/vpp/+/47056>`_ [VECr 14]: build: Changes in makefiles to enabe build on FreeBSD

emacs: **Dave Barach** <vpp@barachs.net>
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader

ethernet: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `47211 <https:////gerrit.fd.io/r/c/vpp/+/47211>`_ [VECr 0]: ethernet: compare unaligned MAC addresses

feature: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `46461 <https:////gerrit.fd.io/r/c/vpp/+/46461>`_ [VECr 30]: ipsec: IPTFS (RFC 9347)

fib: **Neale Ranns** <neale@graphiant.com>
  | `48138 <https:////gerrit.fd.io/r/c/vpp/+/48138>`_ [VECr 2]: linux-cp: replace a route's paths when a resync re-adds it
  | `47983 <https:////gerrit.fd.io/r/c/vpp/+/47983>`_ [VECr 5]: fib: make popular path-list transition a one-shot
  | `47076 <https:////gerrit.fd.io/r/c/vpp/+/47076>`_ [VECr 8]: fib: decide the glean source by the address it holds
  | `47116 <https:////gerrit.fd.io/r/c/vpp/+/47116>`_ [VECr 8]: fib: populate the glean on source reactivation
  | `47402 <https:////gerrit.fd.io/r/c/vpp/+/47402>`_ [VECr 24]: fib: fix stale importer pointer in attached-export walk

flow: **Damjan Marion** <damarion@cisco.com>
  | `47056 <https:////gerrit.fd.io/r/c/vpp/+/47056>`_ [VECr 14]: build: Changes in makefiles to enabe build on FreeBSD

flowprobe: **Ole Troan** <otroan@employees.org>
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader

geneve: **community** vpp-dev@lists.fd.io
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader

gtpu: **Hongjun Ni** <hongjun.ni@intel.com>
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader

hs-test: **Florin Coras** <fcoras@cisco.com>, **Matus Fabian** <matfabia@cisco.com>
  | `48254 <https:////gerrit.fd.io/r/c/vpp/+/48254>`_ [VECr 0]: hs-test: stage VPP startup files via volumes
  | `48256 <https:////gerrit.fd.io/r/c/vpp/+/48256>`_ [VECr 0]: hs-test: inspect container state on startup
  | `48240 <https:////gerrit.fd.io/r/c/vpp/+/48240>`_ [VECr 0]: hs-test: run container commands with Docker SDK
  | `48078 <https:////gerrit.fd.io/r/c/vpp/+/48078>`_ [VECr 3]: vlib: fix quoted process state in show runtime
  | `46907 <https:////gerrit.fd.io/r/c/vpp/+/46907>`_ [VECr 8]: fastacl: RFC 8955 FlowSpec filter for volumetric DDoS mitigation

hsa: **Florin Coras** <fcoras@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>
  | `47056 <https:////gerrit.fd.io/r/c/vpp/+/47056>`_ [VECr 14]: build: Changes in makefiles to enabe build on FreeBSD

http_static: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader

idpf: **Jeff Shaw** <jeffrey.b.shaw@intel.com>
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader

ikev2: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Benoît Ganne** <bganne@cisco.com>
  | `47656 <https:////gerrit.fd.io/r/c/vpp/+/47656>`_ [VECr 0]: ikev2: close a first Child SA the initiator cannot install
  | `48253 <https:////gerrit.fd.io/r/c/vpp/+/48253>`_ [VECr 0]: ikev2: reply to ikev2_nonce_get of unknown SA
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader
  | `47862 <https:////gerrit.fd.io/r/c/vpp/+/47862>`_ [VECr 8]: ikev2: add RFC 7427 digital signature authentication
  | `46461 <https:////gerrit.fd.io/r/c/vpp/+/46461>`_ [VECr 30]: ipsec: IPTFS (RFC 9347)

interface: **Dave Barach** <vpp@barachs.net>
  | `48231 <https:////gerrit.fd.io/r/c/vpp/+/48231>`_ [VECr 0]: interface: convert cli commands
  | `48148 <https:////gerrit.fd.io/r/c/vpp/+/48148>`_ [VECr 2]: ip: move IPv6 specials when binding an enabled interface
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader

ioam: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader
  | `46955 <https:////gerrit.fd.io/r/c/vpp/+/46955>`_ [VECr 7]: ip6: fix Pad1 off-by-one in hop-by-hop option pars

ip-neighbor: **Neale Ranns** <neale@graphiant.com>
  | `47273 <https:////gerrit.fd.io/r/c/vpp/+/47273>`_ [VECr 30]: ip-neighbor: add neighbour table event counters

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader
  | `47947 <https:////gerrit.fd.io/r/c/vpp/+/47947>`_ [VECr 3]: ip: fix IPv6 SVR total payload length
  | `46955 <https:////gerrit.fd.io/r/c/vpp/+/46955>`_ [VECr 7]: ip6: fix Pad1 off-by-one in hop-by-hop option pars
  | `47944 <https:////gerrit.fd.io/r/c/vpp/+/47944>`_ [VECr 7]: ip: clear l4_hdr_truncated bit in ip4 sv-reass
  | `47945 <https:////gerrit.fd.io/r/c/vpp/+/47945>`_ [VECr 7]: ip: tolerate a NULL total_ip_payload_length in sv-reass lock
  | `47946 <https:////gerrit.fd.io/r/c/vpp/+/47946>`_ [VECr 7]: ip: parse the output-arc IPv6 header in sv-reass update
  | `47808 <https:////gerrit.fd.io/r/c/vpp/+/47808>`_ [VECr 11]: ip6: keep the custom app error next across ICMP setup
  | `47445 <https:////gerrit.fd.io/r/c/vpp/+/47445>`_ [VECr 18]: ip6: fix show ip6-ll interface selector
  | `47383 <https:////gerrit.fd.io/r/c/vpp/+/47383>`_ [VECr 27]: ip: fix IPv6 SVR total payload length
  | `46461 <https:////gerrit.fd.io/r/c/vpp/+/46461>`_ [VECr 30]: ipsec: IPTFS (RFC 9347)

ip6-nd: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader
  | `45046 <https:////gerrit.fd.io/r/c/vpp/+/45046>`_ [VECr 18]: ip6-nd: make Neighbor Advertisement punting configurable

ip_session_redirect: **Benoît Ganne** <bganne@cisco.com>
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader

ipfix-export: **Ole Troan** <otroan@employees.org>, **Paul Atkins** <patkins@graphiant.com>
  | `47979 <https:////gerrit.fd.io/r/c/vpp/+/47979>`_ [VECr 6]: ipfix-export: fix mismatched types for time() value

ipsec: **Neale Ranns** <neale@graphiant.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader
  | `47809 <https:////gerrit.fd.io/r/c/vpp/+/47809>`_ [VECr 11]: ipsec: drop a malformed IPv6 AH packet in AH decrypt
  | `47696 <https:////gerrit.fd.io/r/c/vpp/+/47696>`_ [VECr 15]: crypto: retain contexts until asynchronous work completes
  | `46461 <https:////gerrit.fd.io/r/c/vpp/+/46461>`_ [VECr 30]: ipsec: IPTFS (RFC 9347)

l2: **John Lo** <lojultra2020@outlook.com>, **Steven Luong** <sluong@cisco.com>
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader

lacp: **Steven Luong** <sluong@cisco.com>
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader

lb: **Pfister** <ppfister@cisco.com>, **Hongjun Ni** <hongjun.ni@intel.com>
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader
  | `46527 <https:////gerrit.fd.io/r/c/vpp/+/46527>`_ [VECr 20]: lb: add NAT6_NOPORT encap type
  | `46526 <https:////gerrit.fd.io/r/c/vpp/+/46526>`_ [VECr 20]: lb: fix NAT66 UDP/IPv6 checksum zero-fold

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `48208 <https:////gerrit.fd.io/r/c/vpp/+/48208>`_ [VECr 0]: linux-cp: force the netlink socket's receive buffer size
  | `48151 <https:////gerrit.fd.io/r/c/vpp/+/48151>`_ [VECr 1]: linux-cp: copy gratuitous ARP requests to host
  | `48150 <https:////gerrit.fd.io/r/c/vpp/+/48150>`_ [VECr 2]: linux-cp: open the default netns by name when opening netlink sockets
  | `48138 <https:////gerrit.fd.io/r/c/vpp/+/48138>`_ [VECr 2]: linux-cp: replace a route's paths when a resync re-adds it
  | `47866 <https:////gerrit.fd.io/r/c/vpp/+/47866>`_ [VECr 7]: linux-cp: remove the routes of a deleted nexthop object
  | `47814 <https:////gerrit.fd.io/r/c/vpp/+/47814>`_ [VECr 8]: linux-cp: sync interface state when creating a pair

lisp: **Florin Coras** <fcoras@cisco.com>
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader

lldp: **Klement Sekera** <klement.sekera@gmail.com>
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader

mactime: **Dave Barach** <vpp@barachs.net>
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader

mdata: **Dave Barach** <vpp@barachs.net>
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader

memif: **Damjan Marion** <damarion@cisco.com>
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `48216 <https:////gerrit.fd.io/r/c/vpp/+/48216>`_ [VECr 0]: ssh: annotate coverity false positives
  | `48243 <https:////gerrit.fd.io/r/c/vpp/+/48243>`_ [VECr 0]: sr: fix stack overflow in SR MPLS color table
  | `48248 <https:////gerrit.fd.io/r/c/vpp/+/48248>`_ [VECr 0]: sr: fix label stack of SR MPLS policy paths
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 3]: pppoeclient: add PPPoE client plugin
  | `47423 <https:////gerrit.fd.io/r/c/vpp/+/47423>`_ [VECr 4]: bfd: add S-BFD reflector configuration
  | `46907 <https:////gerrit.fd.io/r/c/vpp/+/46907>`_ [VECr 8]: fastacl: RFC 8955 FlowSpec filter for volumetric DDoS mitigation
  | `47274 <https:////gerrit.fd.io/r/c/vpp/+/47274>`_ [VECr 8]: freebsd-cp: FreeBSD Control Plane plugin similar to Linux CP plugin but siginificantly simplified
  | `47056 <https:////gerrit.fd.io/r/c/vpp/+/47056>`_ [VECr 14]: build: Changes in makefiles to enabe build on FreeBSD
  | `46461 <https:////gerrit.fd.io/r/c/vpp/+/46461>`_ [VECr 30]: ipsec: IPTFS (RFC 9347)

mlx5: **Damjan Marion** <dmarion@0xa5.net>
  | `48265 <https:////gerrit.fd.io/r/c/vpp/+/48265>`_ [VECr 0]: mlx5: flush the tx doorbell on x86

mss_clamp: **Miklos Tirpak** <miklos.tirpak@emnify.com>
  | `47476 <https:////gerrit.fd.io/r/c/vpp/+/47476>`_ [VECr 6]: mss_clamp: reset interface state on interface delete

nat: **Ole Troan** <otroan@employees.org>, **Filip Varga** <fivarga@cisco.com>, **Klement Sekera** <klement.sekera@gmail.com>
  | `48250 <https:////gerrit.fd.io/r/c/vpp/+/48250>`_ [VECr 0]: nat: fix NAT44 EI session dump when disabled
  | `47252 <https:////gerrit.fd.io/r/c/vpp/+/47252>`_ [VECr 0]: nat: select dynamic translation by source prefix
  | `47872 <https:////gerrit.fd.io/r/c/vpp/+/47872>`_ [VECr 9]: nat: seed nat64 port allocation at initialization

npol: **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Hedi Bouattour** <hedibouattour2010@gmail.com>
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader

nsh: **Hongjun Ni** <hongjun.ni@intel.com>, **Vengada** <venggovi@cisco.com>
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader
  | `46955 <https:////gerrit.fd.io/r/c/vpp/+/46955>`_ [VECr 7]: ip6: fix Pad1 off-by-one in hop-by-hop option pars

nsim: **Dave Barach** <vpp@barachs.net>
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader

oddbuf: **Dave Barach** <vpp@barachs.net>
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader

papi: **Ole Troan** <otroan@employees.org>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `48235 <https:////gerrit.fd.io/r/c/vpp/+/48235>`_ [VECr 0]: papi: reuse the socket context header
  | `47056 <https:////gerrit.fd.io/r/c/vpp/+/47056>`_ [VECr 14]: build: Changes in makefiles to enabe build on FreeBSD
  | `46982 <https:////gerrit.fd.io/r/c/vpp/+/46982>`_ [VECr 15]: papi: read stats scalars and gauges when they are accessed
  | `47668 <https:////gerrit.fd.io/r/c/vpp/+/47668>`_ [VECr 15]: papi: derive the stats ring metadata stride

pg: **Dave Barach** <vpp@barachs.net>
  | `47916 <https:////gerrit.fd.io/r/c/vpp/+/47916>`_ [VECr 7]: pg: VPP crashing when a non-existing interface provided to 'packet-generator new ...'

pppoe: **Hongjun Ni** <hongjun.ni@intel.com>
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader
  | `47992 <https:////gerrit.fd.io/r/c/vpp/+/47992>`_ [VECr 6]: pppoe: fix local mac of session on sub-interface
  | `47991 <https:////gerrit.fd.io/r/c/vpp/+/47991>`_ [VECr 6]: pppoe: fix message id of session details

pvti: **Andrew Yourtchenko** <ayourtch@gmail.com>
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader

qat: **Damjan Marion** <dmarion@0xa5.net>
  | `48226 <https:////gerrit.fd.io/r/c/vpp/+/48226>`_ [VECr 0]: qat: convert cli commands

quic: **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Florin Coras** <fcoras@cisco.com>
  | `46315 <https:////gerrit.fd.io/r/c/vpp/+/46315>`_ [VECr 6]: quic: quic_quicly add uso support

rdma: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader
  | `45505 <https:////gerrit.fd.io/r/c/vpp/+/45505>`_ [VECr 8]: rdma: add mlx5 dv tso support for raw packet tx

selog: **Mohammed Hawari** <mohammed@hawari.fr>
  | `48251 <https:////gerrit.fd.io/r/c/vpp/+/48251>`_ [VECr 0]: selog: validate the event type index

session: **Florin Coras** <fcoras@cisco.com>
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader
  | `47056 <https:////gerrit.fd.io/r/c/vpp/+/47056>`_ [VECr 14]: build: Changes in makefiles to enabe build on FreeBSD

sfdp: **Mohammed Hawari** <mohammed@hawari.fr>, **Hadi Rayan Al-Sandid** <halsandi@cisco.com>, **Guillaume Solignac** <gsoligna@cisco.com>, **Ole Troan** <otroan@employees.org>
  | `47894 <https:////gerrit.fd.io/r/c/vpp/+/47894>`_ [VECr 0]: sfdp: per-tenant pre-filter for new sessions

sfdp_services_sample: **Mohammed Hawari** <mohammed@hawari.fr>, **Hadi Rayan Al-Sandid** <halsandi@cisco.com>, **Guillaume Solignac** <gsoligna@cisco.com>
  | `47894 <https:////gerrit.fd.io/r/c/vpp/+/47894>`_ [VECr 0]: sfdp: per-tenant pre-filter for new sessions

sflow: **Pim van Pelt** <pim@ipng.nl>, **Neil McKee** <neil.mckee@inmon.com>
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader

snort: **Damjan Marion** <damarion@cisco.com>
  | `48252 <https:////gerrit.fd.io/r/c/vpp/+/48252>`_ [VECr 0]: snort: validate indices in API get handlers
  | `47231 <https:////gerrit.fd.io/r/c/vpp/+/47231>`_ [VECr 5]: snort: consume the enqueue event before clearing interrupt_pending

spdk: **Jerome Tollet** <jtollet@cisco.com>
  | `47874 <https:////gerrit.fd.io/r/c/vpp/+/47874>`_ [VECr 0]: spdk: allow explicit nvme pci attach via vfio
  | `47384 <https:////gerrit.fd.io/r/c/vpp/+/47384>`_ [VECr 19]: spdk: remove obsolete RX prototype state
  | `46736 <https:////gerrit.fd.io/r/c/vpp/+/46736>`_ [VECr 19]: spdk: consume fifo-backed deferred rx batches

sr: **Pablo Camarillo** <pcamaril@cisco.com>, **Ahmed Abdelsalam** <ahabdels@cisco.com>
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader

stn: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader

svm: **Dave Barach** <vpp@barachs.net>
  | `47909 <https:////gerrit.fd.io/r/c/vpp/+/47909>`_ [VECr 8]: api: Modify shared memory handling to support FreeBSD

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `46579 <https:////gerrit.fd.io/r/c/vpp/+/46579>`_ [VECr 0]: misc: patch to test maketest action timeout
  | `48271 <https:////gerrit.fd.io/r/c/vpp/+/48271>`_ [VECr 0]: tests: reuse input pcaps in punt tests
  | `48237 <https:////gerrit.fd.io/r/c/vpp/+/48237>`_ [VECr 0]: tests: probe ipv6 readiness in vm tests
  | `48270 <https:////gerrit.fd.io/r/c/vpp/+/48270>`_ [VECr 0]: tests: reuse input pcaps in mgre tests
  | `47656 <https:////gerrit.fd.io/r/c/vpp/+/47656>`_ [VECr 0]: ikev2: close a first Child SA the initiator cannot install
  | `48188 <https:////gerrit.fd.io/r/c/vpp/+/48188>`_ [VECr 0]: tests: wait for the iperf server socket
  | `47894 <https:////gerrit.fd.io/r/c/vpp/+/47894>`_ [VECr 0]: sfdp: per-tenant pre-filter for new sessions
  | `48208 <https:////gerrit.fd.io/r/c/vpp/+/48208>`_ [VECr 0]: linux-cp: force the netlink socket's receive buffer size
  | `48244 <https:////gerrit.fd.io/r/c/vpp/+/48244>`_ [VECr 0]: tests: wait for vperf tls, dtls and http listeners
  | `48238 <https:////gerrit.fd.io/r/c/vpp/+/48238>`_ [VECr 0]: tests: remove the fixed delay before each test
  | `48214 <https:////gerrit.fd.io/r/c/vpp/+/48214>`_ [VECr 0]: tests: shorten cli api timeout fixtures
  | `48239 <https:////gerrit.fd.io/r/c/vpp/+/48239>`_ [VECr 0]: tests: wait for vperf tcp listeners
  | `48236 <https:////gerrit.fd.io/r/c/vpp/+/48236>`_ [VECr 0]: nsim: check scheduled and actual release times
  | `48211 <https:////gerrit.fd.io/r/c/vpp/+/48211>`_ [VECr 0]: tests: run igmp host query timers on the vpp clock
  | `47514 <https:////gerrit.fd.io/r/c/vpp/+/47514>`_ [VECr 0]: dhcp: bound client option parsing to the packet
  | `47252 <https:////gerrit.fd.io/r/c/vpp/+/47252>`_ [VECr 0]: nat: select dynamic translation by source prefix
  | `48209 <https:////gerrit.fd.io/r/c/vpp/+/48209>`_ [VECr 1]: abf: clear stale flow hash left by reassembly
  | `48151 <https:////gerrit.fd.io/r/c/vpp/+/48151>`_ [VECr 1]: linux-cp: copy gratuitous ARP requests to host
  | `48150 <https:////gerrit.fd.io/r/c/vpp/+/48150>`_ [VECr 2]: linux-cp: open the default netns by name when opening netlink sockets
  | `48148 <https:////gerrit.fd.io/r/c/vpp/+/48148>`_ [VECr 2]: ip: move IPv6 specials when binding an enabled interface
  | `48138 <https:////gerrit.fd.io/r/c/vpp/+/48138>`_ [VECr 2]: linux-cp: replace a route's paths when a resync re-adds it
  | `48056 <https:////gerrit.fd.io/r/c/vpp/+/48056>`_ [VECr 2]: vpp: rewrite the binary-api CLI using the API descriptors
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 3]: pppoeclient: add PPPoE client plugin
  | `47425 <https:////gerrit.fd.io/r/c/vpp/+/47425>`_ [VECr 4]: bfd: add S-BFD reflector datapath
  | `47423 <https:////gerrit.fd.io/r/c/vpp/+/47423>`_ [VECr 4]: bfd: add S-BFD reflector configuration
  | `47426 <https:////gerrit.fd.io/r/c/vpp/+/47426>`_ [VECr 4]: bfd: reflect S-BFD requests sent over MPLS paths
  | `48029 <https:////gerrit.fd.io/r/c/vpp/+/48029>`_ [VECr 4]: tests: make QEMU interface API timeout configurable
  | `47983 <https:////gerrit.fd.io/r/c/vpp/+/47983>`_ [VECr 5]: fib: make popular path-list transition a one-shot
  | `47992 <https:////gerrit.fd.io/r/c/vpp/+/47992>`_ [VECr 6]: pppoe: fix local mac of session on sub-interface
  | `47991 <https:////gerrit.fd.io/r/c/vpp/+/47991>`_ [VECr 6]: pppoe: fix message id of session details
  | `47476 <https:////gerrit.fd.io/r/c/vpp/+/47476>`_ [VECr 6]: mss_clamp: reset interface state on interface delete
  | `46955 <https:////gerrit.fd.io/r/c/vpp/+/46955>`_ [VECr 7]: ip6: fix Pad1 off-by-one in hop-by-hop option pars
  | `47916 <https:////gerrit.fd.io/r/c/vpp/+/47916>`_ [VECr 7]: pg: VPP crashing when a non-existing interface provided to 'packet-generator new ...'
  | `47866 <https:////gerrit.fd.io/r/c/vpp/+/47866>`_ [VECr 7]: linux-cp: remove the routes of a deleted nexthop object
  | `47816 <https:////gerrit.fd.io/r/c/vpp/+/47816>`_ [VECr 7]: linux-cp: test routes that use nexthop objects
  | `47076 <https:////gerrit.fd.io/r/c/vpp/+/47076>`_ [VECr 8]: fib: decide the glean source by the address it holds
  | `47116 <https:////gerrit.fd.io/r/c/vpp/+/47116>`_ [VECr 8]: fib: populate the glean on source reactivation
  | `46907 <https:////gerrit.fd.io/r/c/vpp/+/46907>`_ [VECr 8]: fastacl: RFC 8955 FlowSpec filter for volumetric DDoS mitigation
  | `47862 <https:////gerrit.fd.io/r/c/vpp/+/47862>`_ [VECr 8]: ikev2: add RFC 7427 digital signature authentication
  | `47274 <https:////gerrit.fd.io/r/c/vpp/+/47274>`_ [VECr 8]: freebsd-cp: FreeBSD Control Plane plugin similar to Linux CP plugin but siginificantly simplified
  | `47707 <https:////gerrit.fd.io/r/c/vpp/+/47707>`_ [VECr 10]: af_packet: set ip4 checksum offload flag
  | `47190 <https:////gerrit.fd.io/r/c/vpp/+/47190>`_ [VECr 12]: af_packet: preserve VLAN TPID when restoring stripped tags
  | `47696 <https:////gerrit.fd.io/r/c/vpp/+/47696>`_ [VECr 15]: crypto: retain contexts until asynchronous work completes
  | `46982 <https:////gerrit.fd.io/r/c/vpp/+/46982>`_ [VECr 15]: papi: read stats scalars and gauges when they are accessed
  | `47623 <https:////gerrit.fd.io/r/c/vpp/+/47623>`_ [VECr 16]: af_packet: fix polling queue count on new queues
  | `47601 <https:////gerrit.fd.io/r/c/vpp/+/47601>`_ [VECr 17]: urpf: don't crash deleting a table with urpf-accept entries
  | `45046 <https:////gerrit.fd.io/r/c/vpp/+/45046>`_ [VECr 18]: ip6-nd: make Neighbor Advertisement punting configurable
  | `47512 <https:////gerrit.fd.io/r/c/vpp/+/47512>`_ [VECr 19]: ipip: fix test assertions
  | `47513 <https:////gerrit.fd.io/r/c/vpp/+/47513>`_ [VECr 19]: tests: fix mtu test assertions
  | `46527 <https:////gerrit.fd.io/r/c/vpp/+/46527>`_ [VECr 20]: lb: add NAT6_NOPORT encap type
  | `46728 <https:////gerrit.fd.io/r/c/vpp/+/46728>`_ [VECr 29]: ipsec: IPTFS (RFC 9347) unit tests
  | `47273 <https:////gerrit.fd.io/r/c/vpp/+/47273>`_ [VECr 30]: ip-neighbor: add neighbour table event counters

tls: **Florin Coras** <fcoras@cisco.com>, **Ping Yu** <ping.yu@intel.com>
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader

tm: **Venkata Ravichandra Mynidi** <vmynidi@marvell.com>, **Alok Mishra** <almishra@marvell.com>
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader

tracenode: **Maxime Peim** <mpeim@cisco.com>
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader

unittest: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `48232 <https:////gerrit.fd.io/r/c/vpp/+/48232>`_ [VECr 0]: unittest: cut overhead in the bihash thread test
  | `46955 <https:////gerrit.fd.io/r/c/vpp/+/46955>`_ [VECr 7]: ip6: fix Pad1 off-by-one in hop-by-hop option pars
  | `47696 <https:////gerrit.fd.io/r/c/vpp/+/47696>`_ [VECr 15]: crypto: retain contexts until asynchronous work completes
  | `47450 <https:////gerrit.fd.io/r/c/vpp/+/47450>`_ [VECr 22]: rdma: add cloned TX packet probe
  | `47402 <https:////gerrit.fd.io/r/c/vpp/+/47402>`_ [VECr 24]: fib: fix stale importer pointer in attached-export walk
  | `46461 <https:////gerrit.fd.io/r/c/vpp/+/46461>`_ [VECr 30]: ipsec: IPTFS (RFC 9347)

urpf: **Neale Ranns** <neale@graphiant.com>
  | `47601 <https:////gerrit.fd.io/r/c/vpp/+/47601>`_ [VECr 17]: urpf: don't crash deleting a table with urpf-accept entries

vapi: **Ole Troan** <otroan@employees.org>
  | `47635 <https:////gerrit.fd.io/r/c/vpp/+/47635>`_ [VECr 16]: vapi: Incorrect handling EAGAIN on unix domain socket transport

vat: **Dave Barach** <vpp@barachs.net>
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader

vat2: **Ole Troan** <otroan@employees.org>
  | `47510 <https:////gerrit.fd.io/r/c/vpp/+/47510>`_ [VECr 0]: vat2: bound and fail-closed the JSON file read

vhost: **Steven Luong** <sluong@cisco.com>
  | `48119 <https:////gerrit.fd.io/r/c/vpp/+/48119>`_ [VECr 0]: vhost: fix guest memory region lookup on aarch64
  | `48118 <https:////gerrit.fd.io/r/c/vpp/+/48118>`_ [VECr 0]: vhost: fix crash on invalid descriptor length
  | `47736 <https:////gerrit.fd.io/r/c/vpp/+/47736>`_ [VECr 0]: vhost: fix crash on invalid rx offload metadata

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `47205 <https:////gerrit.fd.io/r/c/vpp/+/47205>`_ [VECr 0]: vlib: avoid null pointer arithmetic in main walk
  | `48255 <https:////gerrit.fd.io/r/c/vpp/+/48255>`_ [VECr 0]: vlib: write the memory trace JSON with clib_json
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader
  | `48078 <https:////gerrit.fd.io/r/c/vpp/+/48078>`_ [VECr 3]: vlib: fix quoted process state in show runtime
  | `47823 <https:////gerrit.fd.io/r/c/vpp/+/47823>`_ [VECr 10]: vlib: align trace data to cache line
  | `47056 <https:////gerrit.fd.io/r/c/vpp/+/47056>`_ [VECr 14]: build: Changes in makefiles to enabe build on FreeBSD

vmxnet3: **Steven Luong** <sluong@cisco.com>
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader

vperf: **Florin Coras** <fcoras@cisco.com>, **Matus Fabian** <matfabia@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `47056 <https:////gerrit.fd.io/r/c/vpp/+/47056>`_ [VECr 14]: build: Changes in makefiles to enabe build on FreeBSD

vpp: **Dave Barach** <vpp@barachs.net>
  | `48056 <https:////gerrit.fd.io/r/c/vpp/+/48056>`_ [VECr 2]: vpp: rewrite the binary-api CLI using the API descriptors
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader

vpp_config: **John DeNisco** <jdenisco@cisco.com>
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader

vppapigen: **Ole Troan** <otroan@employees.org>
  | `47253 <https:////gerrit.fd.io/r/c/vpp/+/47253>`_ [VECr 0]: vppapigen: support output plugins on Python 3.15
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `48259 <https:////gerrit.fd.io/r/c/vpp/+/48259>`_ [VECr 0]: vppinfra: let a CLI value select further arguments
  | `47697 <https:////gerrit.fd.io/r/c/vpp/+/47697>`_ [VECr 0]: vppinfra: define the shifts of x86 u8x16_load_partial
  | `48262 <https:////gerrit.fd.io/r/c/vpp/+/48262>`_ [VECr 0]: vppinfra: fix undefined shifts in x86 u8x16_store_partial
  | `48257 <https:////gerrit.fd.io/r/c/vpp/+/48257>`_ [VECr 0]: vppinfra: fix candidate check in CLI unit test
  | `48258 <https:////gerrit.fd.io/r/c/vpp/+/48258>`_ [VECr 0]: vppinfra: fix build of bihash template test
  | `45098 <https:////gerrit.fd.io/r/c/vpp/+/45098>`_ [VECr 0]: dpdk: support async flow offload
  | `47056 <https:////gerrit.fd.io/r/c/vpp/+/47056>`_ [VECr 14]: build: Changes in makefiles to enabe build on FreeBSD
  | `45470 <https:////gerrit.fd.io/r/c/vpp/+/45470>`_ [VECr 30]: vppinfra: add cast to prevent warning

vrrp: **Matthew Smith** <mgsmith@netgate.com>
  | `48064 <https:////gerrit.fd.io/r/c/vpp/+/48064>`_ [VECr 2]: vat: remove vpp_api_test and the vat plugin loader

vxlan: **John Lo** <lojultra2020@outlook.com>, **Steven Luong** <sluong@cisco.com>
  | `47322 <https:////gerrit.fd.io/r/c/vpp/+/47322>`_ [VECr 17]: vxlan: check available headroom

wireguard: **Artem Glazychev** <artem.glazychev@xored.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `47696 <https:////gerrit.fd.io/r/c/vpp/+/47696>`_ [VECr 15]: crypto: retain contexts until asynchronous work completes

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Akeel Ali** <akeelapi@gmail.com>:

  | `45686 <https:////gerrit.fd.io/r/c/vpp/+/45686>`_ [Vec 164]: ip_validate: new plugin to drop packets with invalid addresses

**Akos Orban** <orbanakos2001@gmail.com>:

  | `44995 <https:////gerrit.fd.io/r/c/vpp/+/44995>`_ [VEc 23]: cnat: fix show cnat client showing invalid for client id
  | `45001 <https:////gerrit.fd.io/r/c/vpp/+/45001>`_ [vEC 24]: cnat: fix show cnat translation for specific translation id

**Alexander Chernavin** <chernavin@mts.ru>:

  | `46481 <https:////gerrit.fd.io/r/c/vpp/+/46481>`_ [VeC 79]: acl: add callback hooks for list add/del
  | `43726 <https:////gerrit.fd.io/r/c/vpp/+/43726>`_ [vec 87]: vhost: fix rxvq interrupts triggered because of race

**Andrey Vasilevsky** <anvanster@gmail.com>:

  | `46487 <https:////gerrit.fd.io/r/c/vpp/+/46487>`_ [VeC 56]: nat: look up address-only static mappings with protocol 0

**Anil Kainikara** <anilkumar911@gmail.com>:

  | `46256 <https:////gerrit.fd.io/r/c/vpp/+/46256>`_ [vec 133]: crypto: openssl - check ctx alloc/init in key-add

**Anton Blazhko** <ablazhko@cisco.com>:

  | `45808 <https:////gerrit.fd.io/r/c/vpp/+/45808>`_ [Vec 50]: devices: Convert PIPE to plugin

**Aritra Basu** <aritrbas@cisco.com>:

  | `44350 <https:////gerrit.fd.io/r/c/vpp/+/44350>`_ [VEc 16]: ip6-nd: fix unicast NA handling in ND proxy
  | `46530 <https:////gerrit.fd.io/r/c/vpp/+/46530>`_ [VeC 99]: gha: skip build/test verify jobs for docs-only changes
  | `45705 <https:////gerrit.fd.io/r/c/vpp/+/45705>`_ [Vec 142]: kube-test: support CalicoVPP repo restructure (backward-compatible)
  | `46048 <https:////gerrit.fd.io/r/c/vpp/+/46048>`_ [VeC 149]: tcp: add TCP fast open support (RFC 7413)

**Benoît Ganne** <bganne@cisco.com>:

  | `46368 <https:////gerrit.fd.io/r/c/vpp/+/46368>`_ [VeC 121]: vppinfra: make vec_foreach_pointer empty-safe
  | `46117 <https:////gerrit.fd.io/r/c/vpp/+/46117>`_ [VeC 157]: vppapigen: fix vppapigen depfile without imports
  | `46087 <https:////gerrit.fd.io/r/c/vpp/+/46087>`_ [VeC 158]: cnat: wait for cnat scanner session cleanup

**Damjan Marion** <dmarion@0xa5.net>:

  | `48219 <https:////gerrit.fd.io/r/c/vpp/+/48219>`_ [vEC 0]: vnet: convert cli commands
  | `48049 <https:////gerrit.fd.io/r/c/vpp/+/48049>`_ [vEC 0]: api: render the API JSON from the descriptors
  | `48228 <https:////gerrit.fd.io/r/c/vpp/+/48228>`_ [vEC 0]: arp: convert cli commands
  | `48218 <https:////gerrit.fd.io/r/c/vpp/+/48218>`_ [vEC 0]: flow: convert cli commands
  | `48227 <https:////gerrit.fd.io/r/c/vpp/+/48227>`_ [vEC 0]: vnet: deprecate srp
  | `48221 <https:////gerrit.fd.io/r/c/vpp/+/48221>`_ [vEC 0]: rdma: convert cli commands
  | `47822 <https:////gerrit.fd.io/r/c/vpp/+/47822>`_ [vEC 10]: ipsec: fix tunnel protect cli help

**Dave Wallace** <dwallacelf@gmail.com>:

  | `45941 <https:////gerrit.fd.io/r/c/vpp/+/45941>`_ [vEC 2]: misc: patch to test CI infra

**Dennis Lanov** <dennis.lanov@gmail.com>:

  | `46270 <https:////gerrit.fd.io/r/c/vpp/+/46270>`_ [VeC 134]: acl: correct interface command help

**Denys Haryachyy** <garyachy@gmail.com>:

  | `47058 <https:////gerrit.fd.io/r/c/vpp/+/47058>`_ [VeC 41]: acl: stop counting hash hits in a shared per-entry field

**G. Paul Ziemba** <pz-vpp-dev@ziemba.us>:

  | `45510 <https:////gerrit.fd.io/r/c/vpp/+/45510>`_ [veC 82]: crypto: add op tracing capability
  | `45699 <https:////gerrit.fd.io/r/c/vpp/+/45699>`_ [VeC 111]: dpdk: buffer bug fixes

**Gopalakrishnan Subramani** <gsubramani@idirect.net>:

  | `47023 <https:////gerrit.fd.io/r/c/vpp/+/47023>`_ [veC 48]: igmp: set proxy mfib Accept on host and Forward on router

**GregMiller** <greg@gregmiller.co.za>:

  | `46129 <https:////gerrit.fd.io/r/c/vpp/+/46129>`_ [VeC 156]: pppoe: native per-session rx policing in pppoe-decap node
  | `46125 <https:////gerrit.fd.io/r/c/vpp/+/46125>`_ [VeC 156]: pppoe: add combined subscriber session provisioning API

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [Vec 52]: sfdp: add sfdp-session-stats service
  | `46588 <https:////gerrit.fd.io/r/c/vpp/+/46588>`_ [veC 87]: sfdp_services: various sfdp nat improvements
  | `44847 <https:////gerrit.fd.io/r/c/vpp/+/44847>`_ [VeC 148]: sfdp: modify tenant_index type from u16 to u32
  | `45964 <https:////gerrit.fd.io/r/c/vpp/+/45964>`_ [VeC 155]: flow: add parameter to pre-allocate global pool
  | `45481 <https:////gerrit.fd.io/r/c/vpp/+/45481>`_ [veC 155]: flow: add action VNET_FLOW_ACTION_STEER_TO_PORT
  | `45637 <https:////gerrit.fd.io/r/c/vpp/+/45637>`_ [VeC 155]: dpdk: add support for VNET_FLOW_ACTION_AGE action
  | `45633 <https:////gerrit.fd.io/r/c/vpp/+/45633>`_ [veC 156]: dpdk: add support for represented port action
  | `45482 <https:////gerrit.fd.io/r/c/vpp/+/45482>`_ [Vec 156]: sfdp: add verdict-testbench service
  | `46043 <https:////gerrit.fd.io/r/c/vpp/+/46043>`_ [VeC 156]: flow: add APIs to support new flow actions
  | `45636 <https:////gerrit.fd.io/r/c/vpp/+/45636>`_ [VeC 156]: flow: add flow aging support
  | `45635 <https:////gerrit.fd.io/r/c/vpp/+/45635>`_ [VeC 168]: dpdk: add support for VNET_FLOW_ACTION_COUNT
  | `45634 <https:////gerrit.fd.io/r/c/vpp/+/45634>`_ [VeC 168]: flow: implement VNET_FLOW_ACTION_COUNT operation
  | `45938 <https:////gerrit.fd.io/r/c/vpp/+/45938>`_ [Vec 172]: tracepath: minor refactoring to code

**Hanataba Azaka** <northern.snow.x@gmail.com>:

  | `46041 <https:////gerrit.fd.io/r/c/vpp/+/46041>`_ [VEc 27]: cnat: make session scanner budget configurable

**Hedi Bouattour** <hedibouattour2010@gmail.com>:

  | `46147 <https:////gerrit.fd.io/r/c/vpp/+/46147>`_ [Vec 153]: npol: support prednat policies
  | `45914 <https:////gerrit.fd.io/r/c/vpp/+/45914>`_ [Vec 157]: cnat: preallocate ts_pools to eliminate reader locks on timestamp get

**Janik** <janik.haag@imc.com>:

  | `46122 <https:////gerrit.fd.io/r/c/vpp/+/46122>`_ [Vec 128]: build: fix make install-deps for fedora targets
  | `46123 <https:////gerrit.fd.io/r/c/vpp/+/46123>`_ [VeC 157]: vcl: add regression test for nonblocking connect()
  | `46124 <https:////gerrit.fd.io/r/c/vpp/+/46124>`_ [VeC 157]: vcl: add regression test for ignorable flags
  | `46121 <https:////gerrit.fd.io/r/c/vpp/+/46121>`_ [VeC 157]: sasc: fix gcc uninitialized warning

**Jerome Tollet** <jtollet@cisco.com>:

  | `48264 <https:////gerrit.fd.io/r/c/vpp/+/48264>`_ [VEc 0]: rdma: flush mlx5 tx doorbell on x86
  | `48241 <https:////gerrit.fd.io/r/c/vpp/+/48241>`_ [vEC 0]: tests: wait for vperf cut-through listeners
  | `48215 <https:////gerrit.fd.io/r/c/vpp/+/48215>`_ [vEC 0]: tests: wait for ikev2 dead peer cleanup
  | `48193 <https:////gerrit.fd.io/r/c/vpp/+/48193>`_ [vEC 0]: tests: decouple network names from the test seed
  | `48194 <https:////gerrit.fd.io/r/c/vpp/+/48194>`_ [vEC 1]: tests: overlap af_xdp veth settling
  | `47270 <https:////gerrit.fd.io/r/c/vpp/+/47270>`_ [VeC 32]: build: refresh optional SPDK upstream snapshot

**Jiajun Liang** <3138947285@qq.com>:

  | `47281 <https:////gerrit.fd.io/r/c/vpp/+/47281>`_ [VeC 31]: dhcp: fix PD client crash without link-local

**Jianquan Ye** <jianquanye@microsoft.com>:

  | `45864 <https:////gerrit.fd.io/r/c/vpp/+/45864>`_ [Vec 169]: ip bonding hash: inner-aware flow hash (opt-in)

**Jon Loeliger** <loeliger@gmail.com>:

  | `48196 <https:////gerrit.fd.io/r/c/vpp/+/48196>`_ [vEC 1]: vxlan-gpe: fix mismatched type for time_t value

**Kai Ji** <kai.ji@intel.com>:

  | `46925 <https:////gerrit.fd.io/r/c/vpp/+/46925>`_ [VEc 29]: crypto: fix engine registration and async dispatch
  | `46926 <https:////gerrit.fd.io/r/c/vpp/+/46926>`_ [VeC 52]: dpdk: fix QAT cryptodev AEAD sessions
  | `46927 <https:////gerrit.fd.io/r/c/vpp/+/46927>`_ [VeC 58]: crypto: fix fixed-tag AEAD validation

**Keith Spinney** <kspinney@cisco.com>:

  | `46525 <https:////gerrit.fd.io/r/c/vpp/+/46525>`_ [Vec 52]: fib: barrier-protect fib_path_list_destroy()

**Klement Sekera** <ksekera@netgate.com>:

  | `46963 <https:////gerrit.fd.io/r/c/vpp/+/46963>`_ [VeC 36]: tests: fix fragment_rfc791/fragment_rfc8200 bugs
  | `47177 <https:////gerrit.fd.io/r/c/vpp/+/47177>`_ [VeC 38]: ip: parse the output-arc IPv6 header in sv-reass update
  | `47172 <https:////gerrit.fd.io/r/c/vpp/+/47172>`_ [VeC 40]: ip: clear l4_hdr_truncated bit in ip4 sv-reass
  | `47173 <https:////gerrit.fd.io/r/c/vpp/+/47173>`_ [VeC 40]: ip: tolerate a NULL total_ip_payload_length in sv-reass lock
  | `47020 <https:////gerrit.fd.io/r/c/vpp/+/47020>`_ [VeC 48]: tests: skip parameterized_class base classes in discovery
  | `46789 <https:////gerrit.fd.io/r/c/vpp/+/46789>`_ [veC 48]: test: wait for handoff queues to drain before reading a capture
  | `46995 <https:////gerrit.fd.io/r/c/vpp/+/46995>`_ [VeC 49]: tests: improve return type consistency
  | `46788 <https:////gerrit.fd.io/r/c/vpp/+/46788>`_ [VeC 73]: vlib: add show handoff pending CLI
  | `46013 <https:////gerrit.fd.io/r/c/vpp/+/46013>`_ [VeC 136]: build: include GNUInstallDirs in VPPConfig
  | `45728 <https:////gerrit.fd.io/r/c/vpp/+/45728>`_ [VeC 136]: api: add build-time python stub generation via vppapigen

**Longxiang Lyu** <lolv@microsoft.com>:

  | `45685 <https:////gerrit.fd.io/r/c/vpp/+/45685>`_ [Vec 169]: ipip: add p2ap ipip tunnel
  | `45898 <https:////gerrit.fd.io/r/c/vpp/+/45898>`_ [Vec 169]: ip: add 'no-class-e-drop' startup config option to suppress class E drop route

**Matus Fabian** <mfabianlf@pm.me>:

  | `46284 <https:////gerrit.fd.io/r/c/vpp/+/46284>`_ [VeC 35]: udp: add segmentation offload support

**Maxim Evdokimov** <lonsdevil@gmail.com>:

  | `47200 <https:////gerrit.fd.io/r/c/vpp/+/47200>`_ [VeC 35]: dpdk: fix clib file descriptor leak on admin down

**Maxime Peim** <maxime.peim@gmail.com>:

  | `47701 <https:////gerrit.fd.io/r/c/vpp/+/47701>`_ [vEC 0]: tests: avoid preexec callbacks when pinning iperf
  | `45152 <https:////gerrit.fd.io/r/c/vpp/+/45152>`_ [VeC 175]: dpdk: install default jump-to-group-1 rule for mlx5
  | `45539 <https:////gerrit.fd.io/r/c/vpp/+/45539>`_ [veC 175]: dpdk: multi-thread async flow offload with per-worker caches

**Micha? Czerwonka** <mczka.mczka@gmail.com>:

  | `46900 <https:////gerrit.fd.io/r/c/vpp/+/46900>`_ [VeC 56]: vpp: vpp/vnet/main.c fix parsing vpp option and improve description of usage

**Mohammad Mahdi Nemati Haravani** <nemati.mahdi255@gmail.com>:

  | `44303 <https:////gerrit.fd.io/r/c/vpp/+/44303>`_ [VEc 23]: build: fix vpp-ext-deps install and clean paths

**Mohammed HAWARI** <momohawari@gmail.com>:

  | `42343 <https:////gerrit.fd.io/r/c/vpp/+/42343>`_ [VeC 97]: vcl: LDP default to regular option

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `42886 <https:////gerrit.fd.io/r/c/vpp/+/42886>`_ [Vec 102]: ipip: fix support for ipip6o6 from linux tunnel

**Mykyta Demusenko** <mdemusen@cisco.com>:

  | `46625 <https:////gerrit.fd.io/r/c/vpp/+/46625>`_ [VeC 78]: teib: move the TEIB implementation to a plugin
  | `46602 <https:////gerrit.fd.io/r/c/vpp/+/46602>`_ [Vec 78]: teib: narrow the C API and add a vnet-owned service boundary
  | `46724 <https:////gerrit.fd.io/r/c/vpp/+/46724>`_ [Vec 78]: teib: add tests for the TEIB API

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `45099 <https:////gerrit.fd.io/r/c/vpp/+/45099>`_ [VEc 16]: ip6-nd: add all-dst mode to ND mirror proxy

**Nicolas PLANEL** <nplanel@gmail.com>:

  | `44976 <https:////gerrit.fd.io/r/c/vpp/+/44976>`_ [vec 175]: sfdp: async offload lookup

**Ole Troan** <otroan@employees.org>:

  | `46511 <https:////gerrit.fd.io/r/c/vpp/+/46511>`_ [vEC 16]: stats: add directory command to vpp_get_stats
  | `46920 <https:////gerrit.fd.io/r/c/vpp/+/46920>`_ [VEc 22]: ip: stop forwarding the Ethernet trailer
  | `46434 <https:////gerrit.fd.io/r/c/vpp/+/46434>`_ [VeC 111]: vlib: fix log2 histogram overflow bin writing past the bin vector
  | `46380 <https:////gerrit.fd.io/r/c/vpp/+/46380>`_ [Vec 118]: vppapigen: fix unaligned access to packed messages

**Onong Tayeng** <onong.tayeng@gmail.com>:

  | `46753 <https:////gerrit.fd.io/r/c/vpp/+/46753>`_ [VEc 23]: cnat: prevent SNAT policy aliasing across FIBs
  | `46726 <https:////gerrit.fd.io/r/c/vpp/+/46726>`_ [Vec 64]: cnat: clear stale default SNAT policy pointer
  | `46752 <https:////gerrit.fd.io/r/c/vpp/+/46752>`_ [Vec 72]: cnat: update cnat plugin documentation
  | `46471 <https:////gerrit.fd.io/r/c/vpp/+/46471>`_ [Vec 76]: cnat: improve flow statistics and error coverage

**Pavel Lavrukhin** <danttevip@gmail.com>:

  | `47654 <https:////gerrit.fd.io/r/c/vpp/+/47654>`_ [VEc 0]: ikev2: release a refused rekey and wait for the rekey grace

**Pavlo Piatakov** <ppiatako@cisco.com>:

  | `46760 <https:////gerrit.fd.io/r/c/vpp/+/46760>`_ [VeC 78]: cnat: do not count unsupported IP protocols as session alloc failure

**Peter Morrow** <pdmorrow@gmail.com>:

  | `46954 <https:////gerrit.fd.io/r/c/vpp/+/46954>`_ [Vec 45]: vlib: leave a MANA VF down when taking its netvsc device
  | `46953 <https:////gerrit.fd.io/r/c/vpp/+/46953>`_ [VeC 48]: dpdk: recognise the the MANA VF as a bifurcated device

**Pierre Pfister** <pierre@meter.com>:

  | `46858 <https:////gerrit.fd.io/r/c/vpp/+/46858>`_ [vEC 6]: vlib: resume a process once per suspension

**Poornima Kandhade** <poornika@cisco.com>:

  | `46424 <https:////gerrit.fd.io/r/c/vpp/+/46424>`_ [vEC 13]: sfdp: add lifecycle records to session stats ring

**Qi Zhang** <zzqqqqwq77@gmail.com>:

  | `46458 <https:////gerrit.fd.io/r/c/vpp/+/46458>`_ [veC 89]: vlib: detect freed buffer‑chain on node dispatch for double‑free debug
  | `46643 <https:////gerrit.fd.io/r/c/vpp/+/46643>`_ [veC 89]: vnet: fix double-free in bcast fragment reassembly

**Ram Subramanian** <ram@meter.com>:

  | `46442 <https:////gerrit.fd.io/r/c/vpp/+/46442>`_ [VeC 62]: vnet: install missing vnet headers

**Robert Shearman** <robertshearman@gmail.com>:

  | `45957 <https:////gerrit.fd.io/r/c/vpp/+/45957>`_ [VEc 18]: vlib: ASAN-poison unallocated buffers
  | `45955 <https:////gerrit.fd.io/r/c/vpp/+/45955>`_ [VeC 33]: ip: fix adjacent packet overwrite with ip frags
  | `45954 <https:////gerrit.fd.io/r/c/vpp/+/45954>`_ [VeC 33]: ip: fix adjacent packet overwrite with ip6 frags
  | `46051 <https:////gerrit.fd.io/r/c/vpp/+/46051>`_ [VeC 33]: ip: fix punt socket rx when multiple FDs are ready
  | `44551 <https:////gerrit.fd.io/r/c/vpp/+/44551>`_ [VeC 43]: vppapigen: fix inconsistency in paths JSON
  | `46050 <https:////gerrit.fd.io/r/c/vpp/+/46050>`_ [VeC 65]: ip: fix ip mroute bulk insertion CLI for certain inputs
  | `46019 <https:////gerrit.fd.io/r/c/vpp/+/46019>`_ [vec 123]: misc: fix potential OOB read during flow hash calculations

**Ruben Herold** <ruben@puettmann.net>:

  | `47276 <https:////gerrit.fd.io/r/c/vpp/+/47276>`_ [VEc 1]: arp: fix reply for local address with adj-fib

**Ryan Wolfe** <rnwolfe@google.com>:

  | `46492 <https:////gerrit.fd.io/r/c/vpp/+/46492>`_ [VeC 38]: linux-cp: don't copy an unknown link speed to the host tap

**Samuel Benko** <sbenko@cisco.com>:

  | `45765 <https:////gerrit.fd.io/r/c/vpp/+/45765>`_ [VeC 155]: tls: propagate verify config for dtls

**Sergiy Bachynskyy** <sbachyns@cisco.com>:

  | `46206 <https:////gerrit.fd.io/r/c/vpp/+/46206>`_ [VeC 141]: ipfix: move to a plugin

**Shuzo Ichiyoshi** <deadcafe.beef@gmail.com>:

  | `46180 <https:////gerrit.fd.io/r/c/vpp/+/46180>`_ [VeC 114]: session: check event collector lookups
  | `46355 <https:////gerrit.fd.io/r/c/vpp/+/46355>`_ [VeC 121]: ip: fix fragmentation with negative buffer offset
  | `46178 <https:////gerrit.fd.io/r/c/vpp/+/46178>`_ [VeC 121]: session: validate app for async connect RPC
  | `46352 <https:////gerrit.fd.io/r/c/vpp/+/46352>`_ [VeC 123]: vppinfra: serialize VM map page size lookup
  | `46341 <https:////gerrit.fd.io/r/c/vpp/+/46341>`_ [VeC 126]: hsa: make TLS client CLI MP-safe
  | `46311 <https:////gerrit.fd.io/r/c/vpp/+/46311>`_ [VeC 127]: tcp: handle retransmitted SYN-ACK in TIME-WAIT

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `44249 <https:////gerrit.fd.io/r/c/vpp/+/44249>`_ [VEc 28]: fib: dump by src not only contributing routes
  | `47106 <https:////gerrit.fd.io/r/c/vpp/+/47106>`_ [VEc 29]: vnet: rewrite nodes to check available headroom

**Suresh Sundararaman** <suresh.serc@gmail.com>:

  | `47289 <https:////gerrit.fd.io/r/c/vpp/+/47289>`_ [vEC 2]: tests: add temporary core backtrace crash diagnostic
  | `46516 <https:////gerrit.fd.io/r/c/vpp/+/46516>`_ [vEC 2]: misc: surs patch to test CI infra
  | `46529 <https:////gerrit.fd.io/r/c/vpp/+/46529>`_ [VeC 98]: docs: Get the VPP Source

**Viacheslav Zakharchenko** <vzakharc@cisco.com>:

  | `45807 <https:////gerrit.fd.io/r/c/vpp/+/45807>`_ [Vec 134]: bfd: Introduce vppinfra/callback_data based vnet notifier for FIB/ADJ notifications
  | `45810 <https:////gerrit.fd.io/r/c/vpp/+/45810>`_ [Vec 135]: bfd: Extract to plugin

**Vladimir Lavor** <vlavor@cisco.com>:

  | `46268 <https:////gerrit.fd.io/r/c/vpp/+/46268>`_ [VeC 134]: vlib: expose error severity in stats segment

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `45650 <https:////gerrit.fd.io/r/c/vpp/+/45650>`_ [VEc 6]: flowprobe: count based sampling support

**Vratko Polak** <vrpolak@cisco.com>:

  | `46703 <https:////gerrit.fd.io/r/c/vpp/+/46703>`_ [VeC 70]: buffers: make natural layout always default

**Wei Wang** <weiwa@cisco.com>:

  | `46085 <https:////gerrit.fd.io/r/c/vpp/+/46085>`_ [Vec 154]: tls: tls session resumption code and host stack tests

**Yang Liu** <numbksco@gmail.com>:

  | `46018 <https:////gerrit.fd.io/r/c/vpp/+/46018>`_ [Vec 147]: vppinfra: add loongarch64 architecture support

**Yuto Suzuki** <offside.items03@icloud.com>:

  | `45503 <https:////gerrit.fd.io/r/c/vpp/+/45503>`_ [VEc 3]: ip6-nd: update secondary RA prefixes for subnets
  | `45504 <https:////gerrit.fd.io/r/c/vpp/+/45504>`_ [VEc 3]: ip6-nd: support RDNSS option in IPv6 RA

**amodenko+sbg-github@cisco.com** <amodenko+sbg-github@cisco.com>:

  | `47919 <https:////gerrit.fd.io/r/c/vpp/+/47919>`_ [VEc 8]: vlib: preserve worker timers during node refork

**marek zavodsky** <mazavods@gmail.com>:

  | `48155 <https:////gerrit.fd.io/r/c/vpp/+/48155>`_ [VEc 0]: http: 100 Continue support

**niklesh** <nikleshparshaboina@gmail.com>:

  | `45016 <https:////gerrit.fd.io/r/c/vpp/+/45016>`_ [veC 52]: cnat: add scope_id to session key
  | `46546 <https:////gerrit.fd.io/r/c/vpp/+/46546>`_ [VeC 95]: vlib: re-base the timing wheel when arming an empty wheel

**steven luong** <sluong@cisco.com>:

  | `45756 <https:////gerrit.fd.io/r/c/vpp/+/45756>`_ [Vec 36]: vcl: fix crash when closing listener with pending accepts

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
authors          142
maintainers      127
committers       5
abandoned        0
================ ===

