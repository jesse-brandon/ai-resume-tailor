from domain.resume.pipeline import generate_resume

if __name__ == "__main__":

    with open("sample_job.txt") as f:
        job = f.read()

    result = generate_resume(job)

    print("\n--- GENERATED RESUME ---\n")
    print(result)
