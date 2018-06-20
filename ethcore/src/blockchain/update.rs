// Copyright 2015-2018 Parity Technologies (UK) Ltd.
// This file is part of Parity.

// Parity is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.

// Parity is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.

// You should have received a copy of the GNU General Public License
// along with Parity.  If not, see <http://www.gnu.org/licenses/>.

use std::collections::HashMap;
use ethereum_types::{H256, Bloom};
use header::BlockNumber;
use blockchain::block_info::BlockInfo;
use blockchain::extras::{BlockDetails, BlockReceipts, TransactionAddress};

/// Block extras update info.
pub struct ExtrasUpdate<'a> {
	/// Block info.
	pub info: BlockInfo,
	/// Current block uncompressed rlp bytes
	pub block: &'a [u8],
	/// Modified block hashes.
	pub block_hashes: HashMap<BlockNumber, H256>,
	/// Modified block details.
	pub block_details: HashMap<H256, BlockDetails>,
	/// Modified block receipts.
	pub block_receipts: HashMap<H256, BlockReceipts>,
	/// Modified blocks blooms.
	pub blocks_blooms: Option<(u64, Vec<Bloom>)>,
	/// Modified transaction addresses (None signifies removed transactions).
	pub transactions_addresses: HashMap<H256, Option<TransactionAddress>>,
}

/// Extra information in block insertion.
pub struct ExtrasInsert {
	/// The primitive fork choice before applying finalization rules.
	pub fork_choice: ::engines::ForkChoice,
	/// Is the inserted block considered finalized.
	pub is_finalized: bool,
	/// New block local metadata.
	pub metadata: Option<Vec<u8>>,
}
