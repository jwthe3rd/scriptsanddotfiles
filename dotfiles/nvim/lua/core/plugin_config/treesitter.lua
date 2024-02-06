require 'nvim-treesitter.configs'.setup {

	ensure_installed = {"python", "c", "lua", "rust", "julia", "javascript", "html", "css", "cpp"},

	sync_install = false,
	auto_install = true,
	--[[	highlight = {
		enable = true,
	},--]]
}
