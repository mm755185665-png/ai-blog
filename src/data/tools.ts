export interface Tool {
  name: string;
  slug: string;
  url: string;
  tag: string;
  desc: string;
  category: string;
  categorySlug: string;
}

export const TOOLS: { category: string; slug: string; items: Tool[] }[] = [
  {
    category: 'AI编程工具',
    slug: 'coding',
    items: [
      { name: 'Cursor', slug: 'cursor', desc: '基于 VS Code 的 AI 编程编辑器，内置 Claude/GPT-4', url: 'https://cursor.com', tag: '免费/付费', category: 'AI编程工具', categorySlug: 'coding' },
      { name: 'GitHub Copilot', slug: 'github-copilot', desc: 'GitHub 官方 AI 代码补全，支持所有主流 IDE', url: 'https://github.com/features/copilot', tag: '付费', category: 'AI编程工具', categorySlug: 'coding' },
      { name: 'Windsurf', slug: 'windsurf', desc: 'Codeium 出品的 AI 编程编辑器，免费额度慷慨', url: 'https://codeium.com/windsurf', tag: '免费/付费', category: 'AI编程工具', categorySlug: 'coding' },
      { name: 'Trae', slug: 'trae', desc: '字节跳动出品的 AI 编程工具，国内可直接使用', url: 'https://trae.ai', tag: '免费', category: 'AI编程工具', categorySlug: 'coding' },
      { name: 'CodeGeeX', slug: 'codegeex', desc: '清华出品的免费 AI 编程插件，支持 VS Code/JetBrains', url: 'https://codegeex.cn', tag: '免费', category: 'AI编程工具', categorySlug: 'coding' },
      { name: 'Claude Code', slug: 'claude-code', desc: 'Anthropic 官方 CLI 编程助手，终端直接使用', url: 'https://claude.ai/code', tag: '付费', category: 'AI编程工具', categorySlug: 'coding' },
    ],
  },
  {
    category: 'AI大模型',
    slug: 'models',
    items: [
      { name: 'ChatGPT', slug: 'chatgpt', desc: 'OpenAI 旗舰对话模型，GPT-4o 免费可用', url: 'https://chatgpt.com', tag: '免费/付费', category: 'AI大模型', categorySlug: 'models' },
      { name: 'Claude', slug: 'claude', desc: 'Anthropic 出品，长文本理解和代码能力强', url: 'https://claude.ai', tag: '免费/付费', category: 'AI大模型', categorySlug: 'models' },
      { name: 'DeepSeek', slug: 'deepseek', desc: '国产顶级大模型，免费使用，推理能力强', url: 'https://chat.deepseek.com', tag: '免费', category: 'AI大模型', categorySlug: 'models' },
      { name: 'Gemini', slug: 'gemini', desc: 'Google 出品，与 Google 生态深度集成', url: 'https://gemini.google.com', tag: '免费/付费', category: 'AI大模型', categorySlug: 'models' },
      { name: 'Kimi', slug: 'kimi', desc: '月之暗面出品，长文本处理能力突出', url: 'https://kimi.moonshot.cn', tag: '免费/付费', category: 'AI大模型', categorySlug: 'models' },
      { name: '文心一言', slug: 'wenxin', desc: '百度出品，国内访问稳定，中文理解好', url: 'https://yiyan.baidu.com', tag: '免费', category: 'AI大模型', categorySlug: 'models' },
    ],
  },
  {
    category: 'AI写作工具',
    slug: 'writing',
    items: [
      { name: 'Notion AI', slug: 'notion-ai', desc: 'Notion 内置 AI，写作、总结、翻译一体化', url: 'https://notion.so', tag: '付费', category: 'AI写作工具', categorySlug: 'writing' },
      { name: '秘塔写作猫', slug: 'xiezuocat', desc: '国产 AI 写作助手，中文润色和纠错', url: 'https://xiezuocat.com', tag: '免费/付费', category: 'AI写作工具', categorySlug: 'writing' },
      { name: 'Jasper', slug: 'jasper', desc: '营销文案专用 AI，模板丰富', url: 'https://jasper.ai', tag: '付费', category: 'AI写作工具', categorySlug: 'writing' },
      { name: 'Copy.ai', slug: 'copy-ai', desc: '广告文案和社媒内容生成', url: 'https://copy.ai', tag: '免费/付费', category: 'AI写作工具', categorySlug: 'writing' },
    ],
  },
  {
    category: 'AI图像生成',
    slug: 'image',
    items: [
      { name: 'Midjourney', slug: 'midjourney', desc: '目前最强的 AI 绘画工具，通过 Discord 使用', url: 'https://midjourney.com', tag: '付费', category: 'AI图像生成', categorySlug: 'image' },
      { name: 'DALL·E 3', slug: 'dalle-3', desc: 'OpenAI 出品，集成在 ChatGPT Plus 中', url: 'https://openai.com/dall-e-3', tag: '付费', category: 'AI图像生成', categorySlug: 'image' },
      { name: 'Stable Diffusion', slug: 'stable-diffusion', desc: '开源图像生成模型，可本地部署', url: 'https://stability.ai', tag: '免费', category: 'AI图像生成', categorySlug: 'image' },
      { name: '即梦 AI', slug: 'jimeng', desc: '字节跳动出品，国内可用的 AI 绘画工具', url: 'https://jimeng.jianying.com', tag: '免费/付费', category: 'AI图像生成', categorySlug: 'image' },
      { name: 'Flux', slug: 'flux', desc: '新一代开源图像模型，质量媲美 Midjourney', url: 'https://blackforestlabs.ai', tag: '免费/付费', category: 'AI图像生成', categorySlug: 'image' },
    ],
  },
  {
    category: 'AI视频工具',
    slug: 'video',
    items: [
      { name: 'Sora', slug: 'sora', desc: 'OpenAI 出品的文生视频模型', url: 'https://sora.com', tag: '付费', category: 'AI视频工具', categorySlug: 'video' },
      { name: '可灵 AI', slug: 'kling', desc: '快手出品，国内领先的 AI 视频生成工具', url: 'https://klingai.com', tag: '免费/付费', category: 'AI视频工具', categorySlug: 'video' },
      { name: 'Runway', slug: 'runway', desc: '专业级 AI 视频编辑和生成平台', url: 'https://runwayml.com', tag: '免费/付费', category: 'AI视频工具', categorySlug: 'video' },
      { name: '即梦视频', slug: 'jimeng-video', desc: '字节跳动出品，文生视频，国内可用', url: 'https://jimeng.jianying.com', tag: '免费/付费', category: 'AI视频工具', categorySlug: 'video' },
    ],
  },
  {
    category: 'AI效率工具',
    slug: 'productivity',
    items: [
      { name: 'Perplexity', slug: 'perplexity', desc: 'AI 搜索引擎，带引用来源的智能问答', url: 'https://perplexity.ai', tag: '免费/付费', category: 'AI效率工具', categorySlug: 'productivity' },
      { name: 'Gamma', slug: 'gamma', desc: 'AI 自动生成 PPT 和演示文稿', url: 'https://gamma.app', tag: '免费/付费', category: 'AI效率工具', categorySlug: 'productivity' },
      { name: 'Dify', slug: 'dify', desc: '开源 AI 应用开发平台，快速搭建 AI 工作流', url: 'https://dify.ai', tag: '免费/付费', category: 'AI效率工具', categorySlug: 'productivity' },
      { name: 'Monica', slug: 'monica', desc: '浏览器 AI 助手，网页总结、翻译、写作', url: 'https://monica.im', tag: '免费/付费', category: 'AI效率工具', categorySlug: 'productivity' },
    ],
  },
];

// Flat list for easy lookup
export const ALL_TOOLS: Tool[] = TOOLS.flatMap(cat => cat.items);

export function getToolBySlug(slug: string): Tool | undefined {
  return ALL_TOOLS.find(t => t.slug === slug);
}

export function getSimilarTools(tool: Tool, n = 3): Tool[] {
  return ALL_TOOLS
    .filter(t => t.categorySlug === tool.categorySlug && t.slug !== tool.slug)
    .slice(0, n);
}
