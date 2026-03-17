CREATE TABLE resume_build.resume_section (
    section_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    resume_id UUID,
    section_name TEXT,
    section_order INT,
    CONSTRAINT fk_resume_section_resume FOREIGN KEY (resume_id) REFERENCES resume_build.resume(resume_id)
);
