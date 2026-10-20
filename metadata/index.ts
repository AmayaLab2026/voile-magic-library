import type { Creator } from '../scripts/types/metadata'
import { getAvatarUrlByGithubName } from '../scripts/utils'

/** 文本 */
export const siteName = 'ヴワル魔法図書館'
export const siteShortName = 'Voile Magic Library'
export const siteDescription = '散发着书香的禁忌之识，尽在本馆'
export const brandName = 'AmayaLab'
export const currentYear = new Date().getFullYear()
export const copyright = `Copyright © 2023-${currentYear} ${brandName}`

/** 文档所在目录 */
export const include = ['docs']

/** Repo */
export const githubRepoLink = 'https://github.com'
/** Discord */
export const discordLink = 'https://discord.gg/'

/** 无协议前缀域名 */
export const plainTargetDomain = ''
/** 完整域名 */
export const targetDomain = `https://${plainTargetDomain}`

/** 创作者 */
export const creators: Creator[] = [
  {
    name: '翎奈猫',
    avatar: '',
    username: 'YuukiReina2023',
    title: 'ヴワル魔法図書館馆长',
    desc: '精神药理学家＆开源情报学家，万事通',
    links: [
      { type: 'github', icon: 'github', link: 'https://github.com/YuukiReina2023' },
      { type: 'twitter', icon: 'twitter', link: 'https://twitter.com/YuukiReina2023' },
    ],
    nameAliases: ['YuukiReina', '翎奈猫', 'Any Neko'],
    emailAliases: ['neko@ayaka.moe'],
  },
 
].map<Creator>((c) => {
  c.avatar = c.avatar || getAvatarUrlByGithubName(c.username)
  return c as Creator
})

export const creatorNames = creators.map(c => c.name)
export const creatorUsernames = creators.map(c => c.username || '')
