import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

const BASE = 'https://mm755185665-png.github.io/ai-blog';

export default defineConfig({
  site: 'https://mm755185665-png.github.io',
  base: '/ai-blog',
  trailingSlash: 'always',
  integrations: [
    sitemap({
      // 排除旧路径（重定向页，不应被收录）
      filter: (page) =>
        !page.includes(`${BASE}/posts/`) &&
        !page.includes(`${BASE}/tags/`) &&
        !page.includes(`${BASE}/search/`) &&
        !page.includes(`${BASE}/about/`) &&
        page !== `${BASE}/`,
      // 为中英文页面添加 hreflang
      customPages: [],
      serialize(item) {
        // 中文页面 → 添加英文 alternate
        if (item.url.includes('/zh/posts/')) {
          const enUrl = item.url.replace('/zh/posts/', '/en/posts/');
          item.links = [
            { lang: 'zh-CN', url: item.url },
            { lang: 'en',    url: enUrl },
            { lang: 'x-default', url: item.url },
          ];
        }
        // 英文页面 → 添加中文 alternate
        if (item.url.includes('/en/posts/')) {
          const zhUrl = item.url.replace('/en/posts/', '/zh/posts/');
          item.links = [
            { lang: 'zh-CN', url: zhUrl },
            { lang: 'en',    url: item.url },
            { lang: 'x-default', url: zhUrl },
          ];
        }
        return item;
      },
    }),
  ],
  markdown: {
    shikiConfig: {
      themes: {
        light: 'github-light',
        dark: 'github-dark',
      },
    },
  },
});
