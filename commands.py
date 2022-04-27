from datetime import datetime
day_filter = datetime.now().strftime("%d-%B-%Y")

COMMANDS = {
		"radius": [
			"show radius statistics"
			],
		"cpu": [
			"show processes cpu sort | ex 0.00",
			"show processes cpu platform sorted",
		],
		"memory": [
			"show memory statistics",
			"show memory failures alloc ",
			"show memory summary",
		],
		"subscriber": [
			"show call admission statistics",
			"show sss statistics",
			"show subscriber session",
			"show sss memory",
			"show sss policy profile",
		],
		"platform": [
			"show platform",
			"show platform power",
			"show platform software infrastructure punt",
			"show platform software infrastructure inject",
			"show platform software status control-processor brief",
			"show platform hardware qfp active tcam resource-manager usage",
			"show platform hardware qfp active infrastructure exmem statistics",
			"show platform hardware qfp active datapath utilization summary",
			"show platform software process slot RP active monitor cycles 2 | inc Cpu|Mem",
			"show platform software object-manager fp active statistics",
		],

		"events": [
			f"show monitor event-trace subscriber all-traces merged all | inc {day_filter}"
			]
		
		}