import courseStructure from '../../../course-materials/course-structure.json'

// Generate navigation from course structure config
const level1 = courseStructure.levels.find(l => l.id === "1")!
const meta: Record<string, string> = {}

level1.modules.forEach(module => {
  meta[module.slug] = `${module.id}: ${module.title}`
})

export default meta

