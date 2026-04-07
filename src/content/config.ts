import { defineCollection, z } from 'astro:content';

const postSchema = z.object({
  title: z.string(),
  date: z.coerce.date(),
  tags: z.array(z.string()).default([]),
  difficulty: z.string().default('中级'),
  summary: z.string().optional(),
  cover: z.string().optional(),
});

const postsZh = defineCollection({ type: 'content', schema: postSchema });
const postsEn = defineCollection({ type: 'content', schema: postSchema });

export const collections = { 'posts-zh': postsZh, 'posts-en': postsEn };
