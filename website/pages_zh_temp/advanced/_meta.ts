import courseStructure from '../../../course-materials/course-structure.json'

// Generate navigation from course structure config
const level2 = courseStructure.levels.find(l => l.id === "2")!
const meta: Record<string, string> = {}

level2.modules.forEach(module => {
  meta[module.slug] = `${module.id}: ${module.title}`
})

export default meta

