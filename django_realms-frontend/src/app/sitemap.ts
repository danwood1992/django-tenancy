import { MetadataRoute } from 'next'
 
export default function sitemap(): MetadataRoute.Sitemap {
  return [
    {
      url: 'https://realms.imperisoft.io/signup',
      lastModified: new Date(),
    },
    {
      url: 'https://realms.imperisoft.io/login',
      lastModified: new Date(),
    },
    {
      url: 'https://realms.imperisoft.io/dashboard',
      lastModified: new Date(),
    },
  ]
}