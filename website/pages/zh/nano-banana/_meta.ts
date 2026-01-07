import courseStructure from '../../../../course-materials/course-structure.json'

// Generate navigation from course structure config
const level3 = courseStructure.levels.find(l => l.id === "3")!
const meta: Record<string, string> = {}

level3.modules.forEach(module => {
  meta[module.slug] = `${module.id}: ${module.title_zh}`
})

export default meta
