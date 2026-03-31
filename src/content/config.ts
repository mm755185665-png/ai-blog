import { defineCollection, z } from 'astro:content';

const posts = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    tags: z.array(z.string()).default([]),
    difficulty: z.string().default('中级'),
    summary: z.string().optional(),
  }),
});

export const collections = { posts };
